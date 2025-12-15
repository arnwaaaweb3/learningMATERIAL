
# Error Log (Explained)
```json
[{
	"message": "Source file requires different compiler version (current compiler is 0.4.17+commit.bdeb9e52.Emscripten.clang - note that nightly builds are considered to be strictly less than the released version",
	"explanation": "This is barely a mismatch between your current compiler and the compiler needed to run your smart contract file.",
    "solution": "Check at your Solidity installed extension. Change the version of your compiler to the specific needed version that the files need",
},{
	"message": "no-trailing-whitespace: Line contains trailing whitespace",
	"explanation": "This is basically says that there's a whitespace left in the end of your lines of code. It considered as an empty space that not needed to be compiled within the file.",
    "solution": "Check every the end of your code lines. Make sure that it's not ended up with an empty space. Delete that empty space if you found any.",
}]
```