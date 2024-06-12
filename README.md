# 图片引用检查与删除工具

**简介**：
这个工具旨在帮助开发者高效地管理项目中的图片资源，通过检查图片的引用情况，找出未被使用的图片并提供删除选项。

**功能详细说明**：
- **递归查找 `.xcassets` 文件夹**：能够全面地搜索项目中所有的 `.xcassets` 文件夹，确保不遗漏任何可能的图片资源位置。
- **提取图片资源路径并与代码引用对比**：准确地提取出图片资源的具体路径，并通过对项目中所有 `.m` 文件的遍历，判断图片是否被实际引用。
- **未被引用图片的处理**：清晰地列出所有未被引用的图片名称和路径，方便开发者查看。同时提供删除操作，并在删除成功后给予明确提示。

**使用步骤**：
1. 确保将此代码文件放置在要检查的项目目录下。
2. 打开终端，进入项目目录。
3. 运行脚本，输入项目目录作为参数，例如：`python UnusedImageRemover.py project_directory`。
4. 程序将开始检查图片引用情况，并显示相关信息。
5. 当显示有未被引用的图片时，根据提示输入 `y` 确认删除或 `n` 取消删除操作。

**注意事项**：
- 请确保在运行前对项目中的重要图片资源进行确认，避免误删。
- 若删除过程中遇到错误，会显示相应的错误信息。

希望这个工具能为你的项目开发和资源管理带来便利，让你的项目更加整洁高效！
