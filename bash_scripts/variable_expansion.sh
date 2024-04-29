#!/bin/bash

# Create an empty variable
myvar1=
myvar2=""

# Show the variable
echo "myvar1:  $myvar1"
echo "myvar2:  $myvar2"

myvar2="testing"
echo

# Show a "default" value if null
echo "myvar1:  ${myvar1:-empty}"
echo "myvar2:  ${myvar2:=empty2}"
echo
echo "myvar1:  $myvar1"
echo "myvar2:  $myvar2"
