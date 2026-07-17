# Unknowns Workflow

[English](README.md) | 简体中文

[![skills.sh](https://skills.sh/b/yanmoon321/unknowns-workflow)](https://skills.sh/yanmoon321/unknowns-workflow)

一个用于将隐藏的假设、约束和风险转化为明确决策的 Agent Skill，帮助你在返工成本变高前发现问题。

它会自行选择最小必要阶段：

- **实现前：**盲点扫描、探索、访谈、参考分析，或面向易变决策的实施计划。
- **实现中：**当现实与原计划冲突时，记录带证据的决策偏离。
- **审查或合并前：**生成以结果为中心的说明、验证边界和理解测验。
- **简单任务：**若修改可逆、需求明确且已有本地证据，则不引入不必要的流程。

## 使用方式

直接带着任务调用，让 Skill 决定当前最适合的阶段：

```text
Use $unknowns-workflow to identify the right next stage for this task.
```

如果希望先得到更稳妥的分析，可以这样说：

```text
Use $unknowns-workflow. Find blind spots first; do not change code yet.
```

## 包含的资源

- `references/routing-and-stop-rules.md`：定义阶段选择规则，以及哪些情况必须暂停并向用户确认。
- `references/beginner-guardrails.md`：提供适合新手的请求句式和风险信号。
- `references/question-prioritization.md`：按后果严重程度排列未知项。
- `references/artifact-contracts.md`：定义可长期保存的发现、实施和审查产物。
- `scripts/create_artifact.py`：生成不会覆盖已有文件的 Markdown 产物骨架。

## 致谢与来源

本项目是受 Thariq Shihipar 的《A Field Guide to Fable: Finding Your Unknowns》启发后，对其方法进行的原创工作流化实现。

原帖地址：https://x.com/trq212/article/2073100352921215386

本项目不复制原帖正文或其示例产物。
