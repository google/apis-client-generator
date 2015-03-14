# Setup #

  * Checkout the latest source.
  * Follow the instructions in the README to install all the prerequisites.


# Running from the command line #

```
$ export PYTHONPATH=<client_top>/src:$PYTHONPATH
$ $(/bin/pwd)/googleapis/codegen/generate_library.py  \
  --api_name=buzz --api_version=v1 --language=java --output_dir=/tmp/gen
```

## Command Options ##

The `--help` option will list all the command options.  The most important ones are:

  * --input: A discovery document captured from a discovery service.  You can specify either input or api\_name/api\_version, but not both.
  * --language: <java|gwt|php>: Target language for the generated library (default: 'java')
  * --language\_variant: which option of "language" to generate for.  (default: 'default')
  * --output\_dir: A path to a directory where the generated files will be created.
  * --output\_file: An output file path to contain the archive for the generated library.