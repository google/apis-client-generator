Contents:



# Understand the code #

Read the [About the Code](AddingALanguage.md) page to get a feeling for how the code is structured and how to change it. If you are modifying the code for your own use, feel free to do whatever you want. If you think you have a change to contribute back, read the rest of the document below.

# Overview to Submitting Patches #

  1. Join our [discussion group](http://groups.google.com/group/google-apis-client-generator)
  1. Discuss your proposed change on the mailing list first.
  1. Sign a Contributor License Agreement (see below).
  1. See detailed instructions below describing our process.

# Contributor License Agreements #

We'd love to accept your code patches. Before we can take them, however, we have to jump a couple of legal hurdles.

Please fill out either the individual or corporate Contributor License Agreement.

  * If you are an individual writing original source code and you're sure you own the intellectual property, then you'll need to sign an [individual CLA](http://code.google.com/legal/individual-cla-v1.0.html).
  * If you work for a company that wants to allow you to contribute your work to this client library, then you'll need to sign a [corporate CLA](http://code.google.com/legal/corporate-cla-v1.0.html).

Follow either of the two links above to access the appropriate CLA and instructions for how to sign and return it. Once we receive it, we'll add you to the official list of contributors and be able to accept your patches.


# Code Review Process #

Code reviews are done using the tool [codereview.appspot.com](http://codereview.appspot.com). Note that we are not using the code review system on this project site because it requires code to already be committed.

## Prerequisites ##

  * Download [upload.py](http://codereview.appspot.com/static/upload.py) and optionally add it to your PATH

## Check out the code ##

Clone the source repository as specified on the [Source Tab](http://code.google.com/p/google-apis-client-generator/source/checkout)

## Make your changes ##

The best way to begin is to propose your changes to the discussion group. You are sure to receive suggestions about how to best design a new feature so that it gets accepted.

## Starting the code review ##


After making changes, change to the root directory of the clone, and create a new issue on codereview.appspot.com:
```
upload.py --send_mail -r reviewer@somedomain --cc ...
```

After making more changes, you will want to upload a new patch (assume the issue # is 123456):
```
upload.py --send_mail -i 123456
```


## Committing the code ##

If you are not an official Contributor, after completing the code review process and receiving approval, a Contributor will pull in your changeset into the repository.