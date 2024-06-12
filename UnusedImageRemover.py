import os
import re
import shutil
import sys

def check_and_delete_images(project_dir):
    print("开始检查图片引用情况...")
    xcassets_paths = []  # 保存.xcassets 文件夹路径
    image_paths = []  # 保存图片资源路径
    unref_image_data = {}  # 使用字典来保存未被引用的图片信息

    # 步骤 1：递归查找.xcassets 文件夹
    print("正在递归查找.xcassets 文件夹...")
    for root, dirs, _ in os.walk(project_dir):
        for dir in dirs:
            if dir.endswith('.xcassets'):
                xcassets_paths.append(os.path.join(root, dir))
    print("找到的.xcassets 文件夹路径如下：")
    for path in xcassets_paths:
        print(f"  - {path}")

    # 步骤 2：找到.xcassets 文件夹二级目录的图片资源文件夹，并保存路径
    for xcassets_path in xcassets_paths:
        for root, dirs, _ in os.walk(xcassets_path):
            for dir in dirs:
                if dir.endswith('.imageset'):
                    image_paths.append(os.path.join(root, dir))
    print("找到的图片资源路径如下：")
    for path in image_paths:
        print(f"  - {path}")

    # 步骤 3：提取图片资源文件夹的名称
    image_names = [os.path.splitext(os.path.basename(image_path))[0] for image_path in image_paths]

    # 步骤 4：使用名称遍历查找在.m 代码中没有用到的图片资源
    m_files = [os.path.join(root, file) for root, dirs, files in os.walk(project_dir) for file in files if file.endswith('.m')]
    for image_name in image_names:
        found = False
        for m_file in m_files:
            with open(m_file, 'r') as f:
                content = f.read()
                # 匹配 @"imagename" 形式
                if re.search(r'@"{}"'.format(image_name), content):
                    found = True
                    break
        if not found:
            unref_image_data[image_name] = image_paths[image_names.index(image_name)]

    print("未被引用的图片名称及路径如下：")
    for name, path in unref_image_data.items():
        print(f"  - {name}: {path}")

    # 步骤 6：删除前确认
    if unref_image_data:
        confirm = input("是否确认删除这些未被引用的图片资源？(y/n): ")
        if confirm.lower() == 'y':
            for image_name, image_path in unref_image_data.items():
                try:
                    shutil.rmtree(image_path)
                    print(f"成功删除图片资源: {image_name}")
                except Exception as e:
                    print(f"删除 {image_path} 时出错: {e}")
        else:
            print("已取消删除操作。")
    else:
        print("没有未被引用的图片资源。")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        project_dir = sys.argv[1]
        check_and_delete_images(project_dir)
    else:
        print("请输入正确的工程目录作为参数")
