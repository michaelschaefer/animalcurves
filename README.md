animalcurves
============

This is a small collection of Python scripts for plotting curves that look like animals.

## Usage

In order to use the software you need Python together with the modules numpy and matplotlib installed. 
If that requirements are fulfilled you can run the main script:

<code>./animalcurves.py &lt;animal&gt; \[&lt;export&gt;\]</code>

The first argument has to be replaced by the name of one of the animal files but without the extension `.py`. 
The second argument is optional. If set to 1 or `true` it will make the script create a PNG image with the 
animal's name instead of showing the plot on screen.

## Providing new animals

If you want to add new curves yourself, please feel free to do so. All you have to do is to provide an additional
Python script with the necessary data in the same directory as `animalcurves.py`. The new script must contain
* a variable `T` indicating the end of the plotting range
* an optional variable `N` indicating the number of plotting points
* a function `func_x(t)` with the x coordinates
* a function `func_y(t)` with the y coordinates
