---
applyTo: '.py, .cpp'
---
# Coding Standards and AI Preferences

## 🎯 Core Principles

### File Size Limit
- **CRITICAL**: Each file MUST contain < 40 lines of code
- Split larger implementations into multiple logical files

### Design Standards
- **Single Responsibility**: One class/module = one purpose
- **Clear Boundaries**: Minimal, explicit interfaces between components
- **Dependencies**: Depend on abstractions, not concrete implementations

## ✅ DO's

### Code Quality
- Keep it simple (KISS)
- Don't repeat yourself (DRY)
- Build only what's needed (YAGNI)
- Use descriptive variable names (capitalize first letter)

### Logging
- Use centralized logger with datetime stamps
- Save logs to centralized location

## ❌ DON'Ts

### Never Add Unless Explicitly Requested
- Tests or test files
- Error handling/validation
- Comments or documentation
- Robust checks

### Avoid Anti-patterns
- Deep inheritance hierarchies
- God classes/modules
- Global state
- Circular dependencies
- Method chaining (e.g., `a.b.c()`)
- `print()` statements for logging

## 📋 Data Safety Checklist
- Check data structure existence before operations
- Handle empty collections gracefully

## 🔄 Re-entry Guidelines
For returning after extended absence:
- Record change rationales
- Keep minimal onboarding notes
