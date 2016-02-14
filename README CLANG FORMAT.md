##This branch of Cinder includes experimental integration of the [ClangFormat](http://clang.llvm.org/docs/ClangFormat.html) tool.


See [this Cinder forum thread](https://forum.libcinder.org/topic/cinder-clangformat-style) for more discussion.



----

###Running ClangFormat

**From the Cinder root:**

	python tools/scripts/format.py .

This branch bundles v3.8 of the clang-format binary, since the latest version from Homebrew (v3.7) is missing some needed flags.


**From Xcode:**

Install the [ClangFormat-Xcode plugin](https://github.com/travisjeffery/ClangFormat-Xcode).

**From Visual Studio:**

Install the [clang-format plugin for Visual Studio](http://llvm.org/builds/). (Not sure if this has a late-enough version of the binary...)


###Structure

The main .clang-format file is in the root of the cinder repo.

Third-party library directories that should be ignored have a very simple .clang-format file. This adds some noise to the repo, but it's helpful since it leaves these files along if you run ClangFormat with `-style=file` flags.

###Ignoring Boost Submodule

`include/boost` needs a `.clang-format` fire to be excluded from formats initiated by IDE plugins. Didn't bother forking Cinder's boost repo, so for now just copy a clang-format "ignore" file from another library path:

	cp src/AntTweakBar/.clang-format include/boost
	
	
###TODO

- Windows support in format.py... bundle windows binary?
- Tweak the root `.clang-format` file to minimize the diff.