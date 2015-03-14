# About the Code #

## Overview of the generator ##

The Google APIs library generator is designed to support multiple output languages from a single core.  It consists of three layers
  1. A core library (Generator) which reads API discovery, resolves schema references and builds a model nearer to the concepts found in most languages.
  1. A language specific layer which subclasses Generator. This layer has two functions
    * language appropriate transforms from protocol wire-format names into identifier and class names
    * language specific selection of files to emit. E.g. Java just writes .java files. C++ might write .h and .cc files.
  1. Language (or dialect) specific templates for generating code


The basic flow is:
  * Load schema to build an API model tree. This tree is a nest collection of objects that all have a name/value dictionary at their core. That makes them directly usable in template systems.  For the most part, class and variable names are assigned at this time, by calling methods like ToClassName(), which the language speicific layer might override.
  * Walk the parse tree in the language layer to add language specific annotations.
  * Walk the selected template tree for the language to create output files.
  * Call back to the language specific generator to add additional source files which the main tree-walker cannot generate.


## Generator core ##

The major components are:
  * generate\_library.py: provides the command line shell around the generator. Since the generator library might also be deployed as a web service, all runtime flags are defined here, rather than in any other modules
  * generator.py: provides the discovery parsing and some conveniences
  * library\_writer.py: provides an interface which allows the generator to open files streams that may either go to disk or .ZIP files.
  * template\_helpers.py: enhances the Django templates with some programming language specific formatting. Django was primarily designed for HTML output, so it's output tends to be white space ignorant. We've added some tools to help get indents and line wrapping right for code. If you are concerned with the layout of your generated code, add formatting features here.
  * LANGUAGE\_generator.py: the language specific layer.

## Philosophy ##

We try to minimize the amount of language specific code. The best changes are ones which add N lines to generator.py and subtract 2N lines from other modules. Likewise, we prefer solutions that add to template\_helpers.py and reduce clutter in the language templates.

Testing is key. This tool is used to generate API bindings that people are using in production systems. Any changes will have to pass a suite of regression tests to assess the degree of pain existing users of libraries would have going forward. New _options_ are preferred over new _defaults_. New languages are preferred to style changes of old ones.


# How to actually add a new language #

## API Design Considerations ##

### namespaces and packages ###

You will want to namespace your library to avoid clashes. You have no control over what the API designer will name things. The namespace should include the service name and version. For example, Java uses com.google.api.buzz.

### Request response style ###

Existing libraries for Google APIs use a common style for building requests.

```
Service serviceHandle = new Service(deployment environment specific modifiers)
TypedRequestObject request = service.typedRequestObject(required params)
request.setOptionalParameters(...)
TypedResponseObject response = request.execute()
```

There is a lot of wiggle room in that framework. The required parameters should be in the request constructor, but each language can do the appropriate thing for optional args. They may be setters on the request (GWT), direct field access to the request (Java), a dict of name/value pairs passed into the constructor (Python, JavasScript), or maybe a full builder pattern that makes an immutable request.

Beyond that, there may be multiple execute() methods for different situations. The example shows a direct response, but it is fine to provide an execute with a callback function.
Model Classes

The library should include a data model class for each schema object. After forming requests, the most important part of the library is serializing the model data to and from JSON.  The Java library uses reflection to optimize space. The space/speed trade off is one you have to make. There is no prohibition against providing generator options to provide optimizations for one or the other.
Auth and deployment environment

Libraries get used in a few principle ways, and the integration with the OAuth library must support them
  1. Full OAuth2 for a multi-user app on a server - You must be able to create the serviceHandle once at server start up and use it with a different OAuth tokens on each request.
  1. Native Application - You perform authorization once and use the same OAuth token on each request.  There are OAuth2 and ClientLogin versions of this.

## Doing the work ##

  * Create a new language generator class by looking at java\_generator.py as an example
  * Make a new template directory
  * Make some templates to get a basic bit of code out
  * Submit a code review to get the name of the generator in place
  * Iterate on the templates until you are happy with the style of the surface
  * Iterate on the templates to make the generated code pretty. If you want better code-aware indentation, enhance template\_helpers.py or ask for help.
  * If your generator code is more than 300 lines of python then you might be doing something wrong. Share your design for the new feature on the discussion list and ask for suggestions on how to lift your new code into the base Generator class
  * Test, test test. Any new features will require an appropriate degree of unit tests to go with them. If we can't prove that old features didn't break, a change will be rejected.