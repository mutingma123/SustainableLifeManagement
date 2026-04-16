---
applyTo: '.tex'
---
1. always use latexmk -pdf to compile and use latexmk -c to clean up every byproduct except .pdf and .tex files.
2. compile without any errors or overfulls.
3. to avoid stalling when compiling, use the -interaction=nonstopmode option. This will allow the compiler to continue running even if it encounters errors, and it will print all errors at the end of the compilation process.
4. finally, recompile the .tex file without the -interaction=nonstopmode option to ensure that all errors are properly addressed and that the final output is correct.