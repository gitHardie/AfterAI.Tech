# AfterAI.tech - AI应用方案资源库

![Hexo Version](https://img.shields.io/badge/hexo-6.3.0-blue)
![Auto Update](https://img.shields.io/badge/auto_update-enabled-success)

专为IT从业者打造的AI解决方案聚合平台，自动生成结构化技术博客内容。

## ✨ 核心功能
- **行业方案聚合**：收录200+个AI在DevOps、云原生、数据工程等领域的应用案例
- **自动文档生成**：通过YAML配置自动生成包含技术架构图的Hexo博文
- **方案检索系统**：支持按技术栈（Python/Go/Rust）、应用场景（自动化/监控/测试）等多维度过滤
- **持续集成**：每日自动同步GitHub趋势项目，通过GitHub Actions实现内容更新

## 🛠️ 技术栈
```bash
.
├── hexo-generator-autodoc # 自定义博文生成器
├── ai-solutions/         # 方案配置文件
│   └── solution-template.yml
├── scripts/
│   ├── auto-updater.py   # 方案爬取脚本
│   └── validate.py       # 配置文件校验器
└── docs/
    └── architecture.vsd  # 系统架构图
```

## 🚀 快速开始
```bash
# 克隆仓库
git clone https://github.com/your-account/afterai.tech.git

# 安装依赖
npm install -g hexo-cli
npm install

# 添加新AI方案（按模板创建文件）
cp ai-solutions/solution-template.yml ai-solutions/new-solution.yml

# 本地运行
hexo server --draft
```

## 📌 示例应用
```yaml
# ai-solutions/github-copilot.yml
title: "GitHub Copilot在代码审查中的应用"
domain: "软件开发"
tech_stack: ["AI代码分析", "GitHub Actions"]
use_case: 
  - 自动检测代码漏洞
  - 生成审查报告
architecture: |
  ![架构图](https://picsum.photos/seed/copilot/800/400)
implementation: "通过GitHub App集成到CI/CD流程..."
```

## 🤝 参与贡献
欢迎提交AI应用案例，请遵循：
1. 在`ai-solutions/`目录创建YAML文件
2. 运行校验脚本：`python scripts/validate.py your-file.yml`
3. 提交Pull Request

## License
MIT © [AfterAI Team](https://afterai.tech)