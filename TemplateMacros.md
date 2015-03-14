# Template Macros #

The generator adds several macros to standard Django to make it easier to generate reasonably formatted code. For background, you should understand the Django template system.

## Filters ##

### block\_comment ###

**block\_comment** is a filter which can be wrapped around a block comment
as you would see them in most programming languages and re-wraps the
lines.  It detects the indent and comment lead-in to automagically do the right thing.

```
  /**{% filter block_comment %}
   * Construct a {{ api.className }} instance to connect to the
   * {{ api.className }} service.
   * {% endfilter %}
```


### noblanklines ###

**noblanklines** is a filter which removes any blank lines, or lines just containing white space.


## Tags ##

### call\_template ###

Evalutes the template named 'template\_name.tmpl' with the variable 'bound\_value\_name' bound to value of the variable 'value\_name'.

Example:
```
{% call_template template_name bound_variable_name value_name %}
```


### copyright\_block ###

Emits a standard copyright block.

Example:
```
{% copyright_block %}
```

### emit\_method\_def ###

Invokes the template found in the file named `"_method.tmpl"` with the variable method bound to the value named by the parameter.

```
{% emit_method_def x %}
```

### emit\_enum\_def ###
### emit\_parameter\_def ###
### emit\_resource\_def ###

TBD - see other templates for examples

### indent/endindent ###

A tag pair which causes the included text to be indented one indent level, according to the language setting.

```
{% indent %}{% emit_method_def method %}{% endindent %}
```


### language ###

**language** sets formatting defaults for the given language.  This should be the first tag in any top level template. Refer to the implementation for a list of supported languages and their defaults.

Example:
```
{% language java %}
```