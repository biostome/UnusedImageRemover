# UnusedImageRemover - iOS 项目未使用图片资源清理工具

![1718181219569](https://github.com/biostome/UnusedImageRemover/assets/18594200/59eb38ec-d3a5-416b-be99-eb19fa39158a)

**简介**：
UnusedImageRemover 是一个专门为 iOS 开发者设计的工具，主要用于在 Xcode 项目中查找和清理未被引用的图片资源。


**功能特点**：
- 能够递归查找项目中的 `.xcassets` 文件夹。
- 准确提取图片资源文件夹中的图片名称。
- 在 `.m` 代码、`.xib` 文件和 `.storyboard` 文件中全面搜索图片的引用情况。
- 列出未被引用的图片名称和路径，方便用户确认和操作。

**使用步骤**：
1. 将本工具的代码集成到你的 
iOS 项目中。
2. 打开终端，进入项目目录。
3. 运行工具，输入项目的完整路径作为参数，如：`python UnusedImageRemover.py /path/to/your/project`。
4. 工具会自动进行图片资源的检查和分析。
5. 查看列出的未被引用图片信息，根据需要决定是否删除。

通过使用 UnusedImageRemover，iOS 开发者可以轻松清理项目中冗余的图片资源，提高项目的运行效率和维护便利性。它与 Xcode 项目紧密结合，为开发者提供了高效的图片资源管理解决方案。
