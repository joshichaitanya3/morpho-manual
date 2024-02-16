# Morpho language

<figure id="fig:Postcard">
<div class="centering">
<embed src="../Figures/postcard.png" style="width:6in" />
</div>
<figcaption><span id="fig:Postcard"
label="fig:Postcard"></span>Postcard-sized summary of the
<em>morpho</em> language. </figcaption>
</figure>
<!-- 
<object data="../Figures/postcard.pdf" type="application/pdf" width="700px" height="700px">
    <embed src="../Figures/postcard.pdf">
        <p>This browser does not support PDFs. Please download the PDF to view it: <a href="http://yoursite.com/the.pdf">Download PDF</a>.</p>
    </embed>
</object> -->

The *morpho* language is simple but expressive. If you're familiar with
C-like languages (C, C++, Java, Javascript) you'll find it very natural.
A much more detailed description is provided in Chapter
[Language](../reference/language.md), but a brief summary is provided in the above figure and we provide an overview of key ideas to help you follow the tutorial:

-   **Comments.** Any text after `//` or surrounded by `/``*` and `*``/`
    is a comment and not processed by morpho:

        // This is a comment
        /* This too! */

-   **Variables.** To create a variable, use the `var` keyword; you can
    then assign and use the variable arbitrarily:

        var a = 1
        print a

-   **Functions.** Functions may take parameters, and you call them like
    this:

        print sin(x)

    and declare them like this:

        fn f(x,y) {
            return x^2+y^2
        }

    Some functions take optional arguments, which look like this:

        var a = foo(quiet=true)

-   **Objects.** *Morpho* is deeply object-oriented. Most things in
    morpho are represented as objects, which provide *methods* that you
    can use to control them. Objects are made by *constructor functions*
    that begin with a capital letter (and may take arguments):

        var a = Object()

    Method calls then look like this:

        a.foo()

-   **Collections.** *Morpho* provides a number of collection typesall
    of which are objectsincluding Lists,

        var a = [1,2,3]

    and Dictionaries:

        var b = { "Massachusetts": "Boston", "California": "Sacramento" }

    and Ranges (often used in loops):

        var a = 0..10:2 # all even numbers 0-10 inclusive

    There are many others, including Matrices, Sparse matrices, etc.
