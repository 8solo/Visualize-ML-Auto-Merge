# Visualize-ML-Auto-Merge
## 鸢尾花书开源项目自动合并工具
鸢尾花书开源项目地址: https://github.com/Visualize-ML
## 已实现功能:
1. 项目中各repo的分章节PDF文件按repo名合并成单一PDF, 方便阅读
2. 项目中各repo的嵌套文件路径代码文件合并至repo名文件夹下, 减少文件嵌套层级
3. 遍历项目中各repo依赖包, 写入libs.txt, 方便一次性导入所有依赖包

## 使用方法:
![image](https://user-images.githubusercontent.com/24363184/236681866-4d241ae0-4557-4b58-9279-bd3928b9deec.png)
1. clone 鸢尾花书项目 repo 至本项目文件夹中
2. 运行merge.py, 项目代码及PDF归至MergedBooks文件夹下. 
3. 安装依赖包: pip install -r libs.txt
## MergedBooks文件夹内包含PDF和repo同名文件夹
![image](https://user-images.githubusercontent.com/24363184/236681923-dbedcd97-e401-4d45-ab2e-40526d48297a.png)
## repo同名文件夹包含该repo所有代码文件
![image](https://user-images.githubusercontent.com/24363184/236681934-3cd2ed37-e854-4199-9ea2-e360e157f616.png)
