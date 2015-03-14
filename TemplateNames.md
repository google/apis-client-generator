# Introduction #

The template system walks one or more template trees to produce one or more output files. In the simple case, files with which end in .tmpl are processed as a template, and other files are copied directly to the output tree.  In both cases, the same relative path to the file is preserved.

Some patterns in file paths are treated specially.

# Where to place templates #

language/surface\_path

## The default tree walker ##

Walks everything under templates.

# String replacements in file names #

## `___package___` ##

Gets replaced by the value of the package path. E.g.

```
java/default/templates/___package___/ApiClient.java.tmpl
```
might result in the output file
_com/google/api/services/buzz_/`ApiClient`.java


## `___api_className___` ##
Gets replaced by the class name of the main service class. E.g.

```
java/default/templates/___package___/___api_className___.java.tmpl
```
might result in the output file
_com/google/api/services/buzz/Buzz_.java


## `___models_` ##

Causes this template file to be passed against each of the data models in the API. `___models_` is stripped from the path, and then all other transforms apply.

## `___models_VARIABLE___` ##

Causes this template file to be passed against each of the data models in the API. This portion of the file path is replaced with the value of VARIABLE evaluated for each model.

## `___topLevelModels_VARIABLE___` ##

Like `___models_VARIABLE___` but only for data models which are top level ones. That is, it excludes anonymous inner schemas.