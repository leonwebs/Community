
<!DOCTYPE html>
<HTML>
<HEAD>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">

<script type="text/x-mathjax-config">
    MathJax.Hub.Config({
    extensions: ["tex2jax.js"],
    jax: ["input/LaTeX", "output/HTML-CSS"],
    "HTML-CSS": { availableFonts: ["TeX"] }
    });
</script>

<script type="text/javascript"
    src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>

<style>

@font-face {
  font-family: 'Raleway';
  font-style: normal;
  font-weight: 300;
  src: local('Raleway Light'), local('Raleway-Light'), url(http://fonts.gstatic.com/s/raleway/v9/-_Ctzj9b56b8RgXW8FArifk_vArhqVIZ0nv9q090hN8.woff2) format('woff2');
}
@font-face {
  font-family: 'Raleway';
  font-style: normal;
  font-weight: 400;
  src: local('Raleway'), url(http://fonts.gstatic.com/s/raleway/v9/0dTEPzkLWceF7z0koJaX1A.woff2) format('woff2');
}
@font-face {
  font-family: 'Raleway';
  font-style: normal;
  font-weight: 600;
  src: local('Raleway SemiBold'), local('Raleway-SemiBold'), url(http://fonts.gstatic.com/s/raleway/v9/xkvoNo9fC8O2RDydKj12b_k_vArhqVIZ0nv9q090hN8.woff2) format('woff2');
}
html {
  font-family: sans-serif; /* 1 */
  -ms-text-size-adjust: 100%; /* 2 */
  -webkit-text-size-adjust: 100%; /* 2 */
}
body {
  margin: 0;
}
article,
aside,
details,
figcaption,
figure,
footer,
header,
hgroup,
main,
menu,
nav,
section,
summary {
  display: block;
}
audio,
canvas,
progress,
video {
  display: inline-block; /* 1 */
  vertical-align: baseline; /* 2 */
}
audio:not([controls]) {
  display: none;
  height: 0;
}
[hidden],
template {
  display: none;
}
a:active,
a:hover {
  outline: 0;
}
abbr[title] {
  border-bottom: 1px dotted;
}
b,
strong {
  font-weight: bold;
}
dfn {
  font-style: italic;
}
h1 {
  font-size: 2em;
  margin: 0.67em 0;
}
mark {
  background: #ff0;
  color: #000;
}
small {
  font-size: 80%;
}
sub,
sup {
  font-size: 75%;
  line-height: 0;
  position: relative;
  vertical-align: baseline;
}
sup {
  top: -0.5em;
}
sub {
  bottom: -0.25em;
}
img {
  border: 0;
}
svg:not(:root) {
  overflow: hidden;
}
figure {
  margin: 1em 40px;
}
hr {
  -moz-box-sizing: content-box;
  box-sizing: content-box;
  height: 0;
}
pre {
  overflow: auto;
}
code,
kbd,
pre,
samp {
  font-family: monospace, monospace;
  font-size: 1em;
}
button,
input,
optgroup,
select,
textarea {
  color: inherit; /* 1 */
  font: inherit; /* 2 */
  margin: 0; /* 3 */
}
button {
  overflow: visible;
}
button,
select {
  text-transform: none;
}
button,
html input[type="button"], /* 1 */
input[type="reset"],
input[type="submit"] {
  -webkit-appearance: button; /* 2 */
  cursor: pointer; /* 3 */
}
button[disabled],
html input[disabled] {
  cursor: default;
}
button::-moz-focus-inner,
input::-moz-focus-inner {
  border: 0;
  padding: 0;
}
input {
  line-height: normal;
}
input[type="checkbox"],
input[type="radio"] {
  box-sizing: border-box; /* 1 */
  padding: 0; /* 2 */
}
input[type="number"]::-webkit-inner-spin-button,
input[type="number"]::-webkit-outer-spin-button {
  height: auto;
}
input[type="search"] {
  -webkit-appearance: textfield; /* 1 */
  -moz-box-sizing: content-box;
  -webkit-box-sizing: content-box; /* 2 */
  box-sizing: content-box;
}
input[type="search"]::-webkit-search-cancel-button,
input[type="search"]::-webkit-search-decoration {
  -webkit-appearance: none;
}
fieldset {
  border: 1px solid #c0c0c0;
  margin: 0 2px;
  padding: 0.35em 0.625em 0.75em;
}
legend {
  border: 0; /* 1 */
  padding: 0; /* 2 */
}
textarea {
  overflow: auto;
}
optgroup {
  font-weight: bold;
}
table {
  border-collapse: collapse;
  border-spacing: 0;
}
td,
th {
  padding: 0;
}


/*
* Skeleton V2.0.4
* Copyright 2014, Dave Gamache
* www.getskeleton.com
* Free to use under the MIT license.
* http://www.opensource.org/licenses/mit-license.php
* 12/29/2014
*/
.container {
  position: relative;
  width: 100%;
  max-width: 960px;
  margin: 0 auto;
  padding: 0 20px;
  box-sizing: border-box; }
.column,
.columns {
  width: 100%;
  float: left;
  box-sizing: border-box; }
@media (min-width: 400px) {
  .container {
    width: 85%;
    padding: 0; }
}
@media (min-width: 550px) {
  .container {
    width: 80%; }
  .column,
  .columns {
    margin-left: 4%; }
  .column:first-child,
  .columns:first-child {
    margin-left: 0; }

  .one.column,
  .one.columns                    { width: 4.66666666667%; }
  .two.columns                    { width: 13.3333333333%; }
  .three.columns                  { width: 22%;            }
  .four.columns                   { width: 30.6666666667%; }
  .five.columns                   { width: 39.3333333333%; }
  .six.columns                    { width: 48%;            }
  .seven.columns                  { width: 56.6666666667%; }
  .eight.columns                  { width: 65.3333333333%; }
  .nine.columns                   { width: 74.0%;          }
  .ten.columns                    { width: 82.6666666667%; }
  .eleven.columns                 { width: 91.3333333333%; }
  .twelve.columns                 { width: 100%; margin-left: 0; }

  .one-third.column               { width: 30.6666666667%; }
  .two-thirds.column              { width: 65.3333333333%; }

  .one-half.column                { width: 48%; }

  /* Offsets */
  .offset-by-one.column,
  .offset-by-one.columns          { margin-left: 8.66666666667%; }
  .offset-by-two.column,
  .offset-by-two.columns          { margin-left: 17.3333333333%; }
  .offset-by-three.column,
  .offset-by-three.columns        { margin-left: 26%;            }
  .offset-by-four.column,
  .offset-by-four.columns         { margin-left: 34.6666666667%; }
  .offset-by-five.column,
  .offset-by-five.columns         { margin-left: 43.3333333333%; }
  .offset-by-six.column,
  .offset-by-six.columns          { margin-left: 52%;            }
  .offset-by-seven.column,
  .offset-by-seven.columns        { margin-left: 60.6666666667%; }
  .offset-by-eight.column,
  .offset-by-eight.columns        { margin-left: 69.3333333333%; }
  .offset-by-nine.column,
  .offset-by-nine.columns         { margin-left: 78.0%;          }
  .offset-by-ten.column,
  .offset-by-ten.columns          { margin-left: 86.6666666667%; }
  .offset-by-eleven.column,
  .offset-by-eleven.columns       { margin-left: 95.3333333333%; }

  .offset-by-one-third.column,
  .offset-by-one-third.columns    { margin-left: 34.6666666667%; }
  .offset-by-two-thirds.column,
  .offset-by-two-thirds.columns   { margin-left: 69.3333333333%; }

  .offset-by-one-half.column,
  .offset-by-one-half.columns     { margin-left: 52%; }

}
html {
  font-size: 62.5%; }
body {
  font-size: 1.5em; /* currently ems cause chrome bug misinterpreting rems on body element */
  line-height: 1.6;
  font-weight: 400;
  font-family: "Raleway", "HelveticaNeue", "Helvetica Neue", Helvetica, Arial, sans-serif;
  color: #222; }
h1, h2, h3, h4, h5, h6 {
  margin-top: 0;
  margin-bottom: 2rem;
  font-weight: 300; }
h1 { font-size: 3.6rem; line-height: 1.2;  letter-spacing: -.1rem;}
h2 { font-size: 3.4rem; line-height: 1.25; letter-spacing: -.1rem; }
h3 { font-size: 3.2rem; line-height: 1.3;  letter-spacing: -.1rem; }
h4 { font-size: 2.8rem; line-height: 1.35; letter-spacing: -.08rem; }
h5 { font-size: 2.4rem; line-height: 1.5;  letter-spacing: -.05rem; }
h6 { font-size: 1.5rem; line-height: 1.6;  letter-spacing: 0; }

p {
  margin-top: 0; }
a {
  color: #1EAEDB; }
a:hover {
  color: #0FA0CE; }
.button,
button,
input[type="submit"],
input[type="reset"],
input[type="button"] {
  display: inline-block;
  height: 38px;
  padding: 0 30px;
  color: #555;
  text-align: center;
  font-size: 11px;
  font-weight: 600;
  line-height: 38px;
  letter-spacing: .1rem;
  text-transform: uppercase;
  text-decoration: none;
  white-space: nowrap;
  background-color: transparent;
  border-radius: 4px;
  border: 1px solid #bbb;
  cursor: pointer;
  box-sizing: border-box; }
.button:hover,
button:hover,
input[type="submit"]:hover,
input[type="reset"]:hover,
input[type="button"]:hover,
.button:focus,
button:focus,
input[type="submit"]:focus,
input[type="reset"]:focus,
input[type="button"]:focus {
  color: #333;
  border-color: #888;
  outline: 0; }
.button.button-primary,
button.button-primary,
input[type="submit"].button-primary,
input[type="reset"].button-primary,
input[type="button"].button-primary {
  color: #FFF;
  background-color: #33C3F0;
  border-color: #33C3F0; }
.button.button-primary:hover,
button.button-primary:hover,
input[type="submit"].button-primary:hover,
input[type="reset"].button-primary:hover,
input[type="button"].button-primary:hover,
.button.button-primary:focus,
button.button-primary:focus,
input[type="submit"].button-primary:focus,
input[type="reset"].button-primary:focus,
input[type="button"].button-primary:focus {
  color: #FFF;
  background-color: #1EAEDB;
  border-color: #1EAEDB; }
input[type="email"],
input[type="number"],
input[type="search"],
input[type="text"],
input[type="tel"],
input[type="url"],
input[type="password"],
textarea,
select {
  height: 38px;
  padding: 6px 10px; /* The 6px vertically centers text on FF, ignored by Webkit */
  background-color: #fff;
  border: 1px solid #D1D1D1;
  border-radius: 4px;
  box-shadow: none;
  box-sizing: border-box; }
/* Removes awkward default styles on some inputs for iOS */
input[type="email"],
input[type="number"],
input[type="search"],
input[type="text"],
input[type="tel"],
input[type="url"],
input[type="password"],
textarea {
  -webkit-appearance: none;
     -moz-appearance: none;
          appearance: none; }
textarea {
  min-height: 65px;
  padding-top: 6px;
  padding-bottom: 6px; }
input[type="email"]:focus,
input[type="number"]:focus,
input[type="search"]:focus,
input[type="text"]:focus,
input[type="tel"]:focus,
input[type="url"]:focus,
input[type="password"]:focus,
textarea:focus,
select:focus {
  border: 1px solid #33C3F0;
  outline: 0; }
label,
legend {
  display: block;
  margin-bottom: .5rem;
  font-weight: 600; }
fieldset {
  padding: 0;
  border-width: 0; }
input[type="checkbox"],
input[type="radio"] {
  display: inline; }
label > .label-body {
  display: inline-block;
  margin-left: .5rem;
  font-weight: normal; }
ul {
  list-style: circle inside; }
ol {
  list-style: decimal inside; }
ol, ul {
  padding-left: 0;
  margin-top: 0; }
ul ul,
ul ol,
ol ol,
ol ul {
  margin: 1.5rem 0 1.5rem 3rem;
  font-size: 90%; }
li {
  margin-bottom: 1rem; }
th,
td {
  padding: 12px 15px;
  text-align: left;
  border-bottom: 1px solid #E1E1E1; }
th:first-child,
td:first-child {
  padding-left: 0; }
th:last-child,
td:last-child {
  padding-right: 0; }
button,
.button {
  margin-bottom: 1rem; }
input,
textarea,
select,
fieldset {
  margin-bottom: 1.5rem; }
pre,
blockquote,
dl,
figure,
table,
p,
ul,
ol,
form {
  margin-bottom: 2.5rem; }
.u-full-width {
  width: 100%;
  box-sizing: border-box; }
.u-max-full-width {
  max-width: 100%;
  box-sizing: border-box; }
.u-pull-right {
  float: right; }
.u-pull-left {
  float: left; }
hr {
  margin-top: 3rem;
  margin-bottom: 3.5rem;
  border-width: 0;
  border-top: 1px solid #E1E1E1; }
.container:after,
.row:after,
.u-cf {
  content: "";
  display: table;
  clear: both; }

pre {
  display: block;
  padding: 9.5px;
  margin: 0 0 10px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #333;
  word-break: break-all;
  word-wrap: break-word;
  background-color: #f5f5f5;
  border: 1px solid #ccc;
  border-radius: 4px;
}
code,
kbd,
pre,
samp {
  font-family: Menlo, Monaco, Consolas, "Courier New", monospace;
}
code {
  padding: 2px 4px;
  font-size: 90%;
  color: #c7254e;
  background-color: #f9f2f4;
  border-radius: 4px;
}

@media (min-width: 400px) {}
@media (min-width: 550px) {}
@media (min-width: 750px) {}
@media (min-width: 1000px) {}
@media (min-width: 1200px) {}

</style>

<style>
.hll { background-color: #ffffcc }
.c { color: #408080; font-style: italic } /* Comment */
.err { border: 1px solid #FF0000 } /* Error */
.k { color: #008000; font-weight: bold } /* Keyword */
.o { color: #666666 } /* Operator */
.ch { color: #408080; font-style: italic } /* Comment.Hashbang */
.cm { color: #408080; font-style: italic } /* Comment.Multiline */
.cp { color: #BC7A00 } /* Comment.Preproc */
.cpf { color: #408080; font-style: italic } /* Comment.PreprocFile */
.c1 { color: #408080; font-style: italic } /* Comment.Single */
.cs { color: #408080; font-style: italic } /* Comment.Special */
.gd { color: #A00000 } /* Generic.Deleted */
.ge { font-style: italic } /* Generic.Emph */
.gr { color: #FF0000 } /* Generic.Error */
.gh { color: #000080; font-weight: bold } /* Generic.Heading */
.gi { color: #00A000 } /* Generic.Inserted */
.go { color: #888888 } /* Generic.Output */
.gp { color: #000080; font-weight: bold } /* Generic.Prompt */
.gs { font-weight: bold } /* Generic.Strong */
.gu { color: #800080; font-weight: bold } /* Generic.Subheading */
.gt { color: #0044DD } /* Generic.Traceback */
.kc { color: #008000; font-weight: bold } /* Keyword.Constant */
.kd { color: #008000; font-weight: bold } /* Keyword.Declaration */
.kn { color: #008000; font-weight: bold } /* Keyword.Namespace */
.kp { color: #008000 } /* Keyword.Pseudo */
.kr { color: #008000; font-weight: bold } /* Keyword.Reserved */
.kt { color: #B00040 } /* Keyword.Type */
.m { color: #666666 } /* Literal.Number */
.s { color: #BA2121 } /* Literal.String */
.na { color: #7D9029 } /* Name.Attribute */
.nb { color: #008000 } /* Name.Builtin */
.nc { color: #0000FF; font-weight: bold } /* Name.Class */
.no { color: #880000 } /* Name.Constant */
.nd { color: #AA22FF } /* Name.Decorator */
.ni { color: #999999; font-weight: bold } /* Name.Entity */
.ne { color: #D2413A; font-weight: bold } /* Name.Exception */
.nf { color: #0000FF } /* Name.Function */
.nl { color: #A0A000 } /* Name.Label */
.nn { color: #0000FF; font-weight: bold } /* Name.Namespace */
.nt { color: #008000; font-weight: bold } /* Name.Tag */
.nv { color: #19177C } /* Name.Variable */
.ow { color: #AA22FF; font-weight: bold } /* Operator.Word */
.w { color: #bbbbbb } /* Text.Whitespace */
.mb { color: #666666 } /* Literal.Number.Bin */
.mf { color: #666666 } /* Literal.Number.Float */
.mh { color: #666666 } /* Literal.Number.Hex */
.mi { color: #666666 } /* Literal.Number.Integer */
.mo { color: #666666 } /* Literal.Number.Oct */
.sa { color: #BA2121 } /* Literal.String.Affix */
.sb { color: #BA2121 } /* Literal.String.Backtick */
.sc { color: #BA2121 } /* Literal.String.Char */
.dl { color: #BA2121 } /* Literal.String.Delimiter */
.sd { color: #BA2121; font-style: italic } /* Literal.String.Doc */
.s2 { color: #BA2121 } /* Literal.String.Double */
.se { color: #BB6622; font-weight: bold } /* Literal.String.Escape */
.sh { color: #BA2121 } /* Literal.String.Heredoc */
.si { color: #BB6688; font-weight: bold } /* Literal.String.Interpol */
.sx { color: #008000 } /* Literal.String.Other */
.sr { color: #BB6688 } /* Literal.String.Regex */
.s1 { color: #BA2121 } /* Literal.String.Single */
.ss { color: #19177C } /* Literal.String.Symbol */
.bp { color: #008000 } /* Name.Builtin.Pseudo */
.fm { color: #0000FF } /* Name.Function.Magic */
.vc { color: #19177C } /* Name.Variable.Class */
.vg { color: #19177C } /* Name.Variable.Global */
.vi { color: #19177C } /* Name.Variable.Instance */
.vm { color: #19177C } /* Name.Variable.Magic */
.il { color: #666666 } /* Literal.Number.Integer.Long */
</style>





<style>
h1.title {margin-top : 20px}
img {max-width : 100%}

#From nbconvert
.ansi-black-fg { color: #3E424D; }
.ansi-black-bg { background-color: #3E424D; }
.ansi-black-intense-fg { color: #282C36; }
.ansi-black-intense-bg { background-color: #282C36; }
.ansi-red-fg { color: #E75C58; }
.ansi-red-bg { background-color: #E75C58; }
.ansi-red-intense-fg { color: #B22B31; }
.ansi-red-intense-bg { background-color: #B22B31; }
.ansi-green-fg { color: #00A250; }
.ansi-green-bg { background-color: #00A250; }
.ansi-green-intense-fg { color: #007427; }
.ansi-green-intense-bg { background-color: #007427; }
.ansi-yellow-fg { color: #DDB62B; }
.ansi-yellow-bg { background-color: #DDB62B; }
.ansi-yellow-intense-fg { color: #B27D12; }
.ansi-yellow-intense-bg { background-color: #B27D12; }
.ansi-blue-fg { color: #208FFB; }
.ansi-blue-bg { background-color: #208FFB; }
.ansi-blue-intense-fg { color: #0065CA; }
.ansi-blue-intense-bg { background-color: #0065CA; }
.ansi-magenta-fg { color: #D160C4; }
.ansi-magenta-bg { background-color: #D160C4; }
.ansi-magenta-intense-fg { color: #A03196; }
.ansi-magenta-intense-bg { background-color: #A03196; }
.ansi-cyan-fg { color: #60C6C8; }
.ansi-cyan-bg { background-color: #60C6C8; }
.ansi-cyan-intense-fg { color: #258F8F; }
.ansi-cyan-intense-bg { background-color: #258F8F; }
.ansi-white-fg { color: #C5C1B4; }
.ansi-white-bg { background-color: #C5C1B4; }
.ansi-white-intense-fg { color: #A1A6B2; }
.ansi-white-intense-bg { background-color: #A1A6B2; }

.ansi-bold { font-weight: bold; }
</style>

</HEAD>
<BODY>
    <div class ="container">
        <div class = "row">
            <div class = "col-md-12 twelve columns">
<h2>Regionalization Analysis</h2>
<h4>Preserving "Communities of Interest"</h4>
<h4>Loading files</h4>
<p>First we import our libraries and load the data files. We'll use
census demographic data to quantify the community of interest. Keeping
the scope narrow, we'll just examine race and ethnicity, but income,
education level, or other indicators may be used.  We also load
current districts to evaluate how well they preserve communities of
interest.  When the redistricting commission produces new districts,
they may be evaluated, too.  Finally, working with the tracts data
takes a lot of time because there are 1250 tracts and the algorithms
are slow.  Setting the global variable currdat to 'counties' lets us
check the code quickly and then resetting it to 'tracts' does what we
want.</p>
<p>The initialization code is at <a href="">helpers/<strong>init</strong>.py</a></p>

<div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">os</span>
<span class="kn">import</span> <span class="nn">sys</span>
<span class="n">sys</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">getcwd</span><span class="p">())</span> <span class="c1"># needed for pweave--why?</span>

<span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="kn">as</span> <span class="nn">plt</span>
<span class="n">orig_backend</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">get_backend</span><span class="p">()</span>
<span class="kn">import</span> <span class="nn">pysal</span> <span class="kn">as</span> <span class="nn">ps</span>
<span class="n">plt</span><span class="o">.</span><span class="n">switch_backend</span><span class="p">(</span><span class="n">orig_backend</span><span class="p">)</span>  <span class="c1">#importing pysal seems to change backend</span>

<span class="kn">import</span> <span class="nn">numpy</span> <span class="kn">as</span> <span class="nn">np</span>
<span class="kn">import</span> <span class="nn">pandas</span> <span class="kn">as</span> <span class="nn">pd</span>
<span class="kn">import</span> <span class="nn">geopandas</span> <span class="kn">as</span> <span class="nn">gpd</span>
<span class="kn">import</span> <span class="nn">region</span>
<span class="kn">from</span> <span class="nn">helpers.objective_functionpopu</span> <span class="kn">import</span> <span class="o">*</span> 
<span class="kn">from</span> <span class="nn">ballpark</span> <span class="kn">import</span> <span class="n">business</span> <span class="k">as</span> <span class="n">human</span>

<span class="kn">from</span> <span class="nn">time</span> <span class="kn">import</span> <span class="n">perf_counter</span> <span class="k">as</span> <span class="n">pfc</span>

<span class="k">def</span> <span class="nf">loaddata</span><span class="p">(</span><span class="n">filename</span><span class="p">,</span> <span class="n">url</span><span class="p">):</span>
    <span class="k">if</span> <span class="ow">not</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">isfile</span><span class="p">(</span><span class="s1">&#39;data/&#39;</span><span class="o">+</span><span class="n">filename</span><span class="o">+</span><span class="s1">&#39;.geojson&#39;</span><span class="p">)):</span>
        <span class="k">print</span><span class="p">(</span><span class="s2">&quot;Retrieving the data and storing to a file&quot;</span><span class="p">)</span>
        <span class="n">geodat</span> <span class="o">=</span> <span class="n">gpd</span><span class="o">.</span><span class="n">read_file</span><span class="p">(</span><span class="n">url</span><span class="p">)</span>
        <span class="n">geodat</span><span class="o">.</span><span class="n">to_file</span><span class="p">(</span><span class="s1">&#39;data/&#39;</span><span class="o">+</span><span class="n">filename</span> <span class="o">+</span> <span class="s1">&#39;.geojson&#39;</span><span class="p">,</span> <span class="n">driver</span><span class="o">=</span><span class="s1">&#39;GeoJSON&#39;</span><span class="p">)</span>
        <span class="n">geodat</span><span class="o">.</span><span class="n">to_file</span><span class="p">(</span><span class="s1">&#39;data/&#39;</span><span class="o">+</span><span class="n">filename</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">geodat</span> <span class="o">=</span> <span class="n">gpd</span><span class="o">.</span><span class="n">read_file</span><span class="p">(</span><span class="s1">&#39;data/&#39;</span><span class="o">+</span><span class="n">filename</span><span class="o">+</span><span class="s1">&#39;.geojson&#39;</span><span class="p">)</span>
    <span class="c1">#convert all to numeric where possible</span>
    <span class="n">geodat</span> <span class="o">=</span> <span class="n">geodat</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="n">pd</span><span class="o">.</span><span class="n">to_numeric</span><span class="p">,</span> <span class="n">errors</span> <span class="o">=</span> <span class="s1">&#39;ignore&#39;</span><span class="p">)</span>
    <span class="c1">#&#39;pop&#39; is not a good name for population</span>
    <span class="k">if</span> <span class="s1">&#39;pop&#39;</span> <span class="ow">in</span> <span class="n">geodat</span><span class="o">.</span><span class="n">columns</span><span class="p">:</span>
        <span class="n">geodat</span><span class="o">.</span><span class="n">rename</span><span class="p">({</span><span class="s1">&#39;pop&#39;</span><span class="p">:</span><span class="s1">&#39;population&#39;</span><span class="p">},</span> <span class="n">axis</span> <span class="o">=</span> <span class="s1">&#39;columns&#39;</span><span class="p">,</span> <span class="n">inplace</span> <span class="o">=</span> <span class="bp">True</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">geodat</span>
<span class="n">files</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;tracts&#39;</span><span class="p">,</span> <span class="s1">&#39;counties&#39;</span><span class="p">,</span> <span class="s1">&#39;districts&#39;</span><span class="p">]</span>
<span class="n">urls</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;https://data.colorado.gov/resource/aevh-apr2.geojson?$limit=1300&#39;</span><span class="p">,</span>
        <span class="s1">&#39;https://data.colorado.gov/resource/ewkj-ipn7.geojson&#39;</span><span class="p">,</span>
        <span class="s1">&#39;https://data.colorado.gov/resource/jz4n-qus2.geojson&#39;</span><span class="p">]</span>
<span class="n">urls</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">(</span><span class="nb">zip</span><span class="p">(</span><span class="n">files</span><span class="p">,</span> <span class="n">urls</span><span class="p">))</span>
<span class="n">geodata</span> <span class="o">=</span> <span class="p">{</span><span class="n">eachfile</span><span class="p">:</span> <span class="n">loaddata</span><span class="p">(</span><span class="n">eachfile</span><span class="p">,</span> <span class="n">urls</span><span class="p">[</span><span class="n">eachfile</span><span class="p">])</span> <span class="k">for</span> <span class="n">eachfile</span> <span class="ow">in</span> <span class="n">files</span><span class="p">}</span>
<span class="n">currdat</span> <span class="o">=</span> <span class="s1">&#39;counties&#39;</span>

<span class="n">badcol</span> <span class="o">=</span> <span class="n">geodata</span><span class="p">[</span><span class="s1">&#39;tracts&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">columns</span><span class="p">[</span><span class="n">geodata</span><span class="p">[</span><span class="s1">&#39;tracts&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">isnull</span><span class="p">()</span><span class="o">.</span><span class="n">any</span><span class="p">()]</span>
<span class="n">racecat</span> <span class="o">=</span> <span class="p">[</span> <span class="s1">&#39;hispanic&#39;</span><span class="p">,</span> <span class="s1">&#39;white_nh&#39;</span><span class="p">,</span> <span class="s1">&#39;black_nh&#39;</span><span class="p">,</span> <span class="s1">&#39;ntvam_nh&#39;</span><span class="p">,</span>
            <span class="s1">&#39;asian_nh&#39;</span><span class="p">,</span> <span class="s1">&#39;hawpi_nh&#39;</span><span class="p">,</span> <span class="s1">&#39;other_nh&#39;</span><span class="p">,</span> <span class="s1">&#39;twoplus_nh&#39;</span><span class="p">]</span>
<span class="c1"># agecat = [i for i in geodata[currdat].columns if &#39;age&#39; in i and i not in badcol]</span>
<span class="c1"># incomecat = []</span>
<span class="c1"># all income categories have some nans!</span>
<span class="c1"># educationcat = [i</span>
<span class="c1">#                 for i in geodata[currdat].columns</span>
<span class="c1">#                 if &#39;gr&#39; in i and i not in badcol]</span>
<span class="c1"># educationcat.extend([&#39;enrolled&#39;, &#39;n_enrolled&#39;])</span>

<span class="n">ndist</span> <span class="o">=</span> <span class="mi">7</span>

<span class="k">def</span> <span class="nf">getpop</span><span class="p">(</span><span class="n">col</span><span class="p">,</span> <span class="n">gdat</span> <span class="o">=</span> <span class="bp">None</span><span class="p">,</span> <span class="n">label</span> <span class="o">=</span> <span class="bp">None</span><span class="p">):</span>
    <span class="k">if</span> <span class="n">gdat</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span>
        <span class="n">gdat</span> <span class="o">=</span> <span class="n">geodata</span><span class="p">[</span><span class="n">currdat</span><span class="p">]</span>
    <span class="k">if</span> <span class="n">label</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span>
        <span class="n">label</span> <span class="o">=</span> <span class="n">geodata</span><span class="p">[</span><span class="n">currdat</span><span class="p">]</span><span class="o">.</span><span class="n">reg_azp</span>
    <span class="k">return</span> <span class="p">[</span><span class="nb">sum</span><span class="p">([</span><span class="n">gdat</span><span class="p">[</span><span class="n">col</span><span class="p">][</span><span class="n">i</span><span class="p">]</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">np</span><span class="o">.</span><span class="n">where</span><span class="p">(</span><span class="n">label</span> <span class="o">==</span> <span class="n">j</span><span class="p">)[</span><span class="mi">0</span><span class="p">]])</span>
            <span class="k">for</span> <span class="n">j</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">1</span><span class="o">+</span><span class="nb">int</span><span class="p">(</span><span class="nb">max</span><span class="p">(</span><span class="n">gdat</span><span class="o">.</span><span class="n">reg_azp</span><span class="p">)))]</span>

<span class="n">regdat</span> <span class="o">=</span> <span class="p">{</span><span class="s1">&#39;counties&#39;</span><span class="p">:</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="s1">&#39;data/countyregions.csv&#39;</span><span class="p">),</span>
          <span class="s1">&#39;tracts&#39;</span><span class="p">:</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="s1">&#39;data/tractregions.csv&#39;</span><span class="p">)}</span>
</pre></div>

<div class="highlight"><pre>
<span class="ansi-red-
fg">---------------------------------------------------------------------------</span><span
class="ansi-red-fg">FileNotFoundError</span>
Traceback (most recent call last)<span class="ansi-green-
fg">&lt;ipython-input-1-384a317964d1&gt;</span> in <span class="ansi-
cyan-fg">&lt;module&gt;</span>
<span class="ansi-green-intense-fg ansi-bold">     61</span>
for j in range(1+int(max(gdat.reg_azp)))]
<span class="ansi-green-intense-fg ansi-bold">     62</span>
<span class="ansi-green-fg">---&gt; 63</span><span class="ansi-red-
fg"> regdat = {&#39;counties&#39;:
pd.read_csv(&#39;data/countyregions.csv&#39;),
</span><span class="ansi-green-intense-fg ansi-bold">     64</span>
&#39;tracts&#39;: pd.read_csv(&#39;data/tractregions.csv&#39;)}
<span class="ansi-green-
fg">/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-
packages/pandas/io/parsers.py</span> in <span class="ansi-cyan-
fg">parser_f</span><span class="ansi-blue-fg">(filepath_or_buffer,
sep, delimiter, header, names, index_col, usecols, squeeze, prefix,
mangle_dupe_cols, dtype, engine, converters, true_values,
false_values, skipinitialspace, skiprows, skipfooter, nrows,
na_values, keep_default_na, na_filter, verbose, skip_blank_lines,
parse_dates, infer_datetime_format, keep_date_col, date_parser,
dayfirst, cache_dates, iterator, chunksize, compression, thousands,
decimal, lineterminator, quotechar, quoting, doublequote, escapechar,
comment, encoding, dialect, error_bad_lines, warn_bad_lines,
delim_whitespace, low_memory, memory_map, float_precision)</span>
<span class="ansi-green-intense-fg ansi-bold">    683</span>         )
<span class="ansi-green-intense-fg ansi-bold">    684</span>
<span class="ansi-green-fg">--&gt; 685</span><span class="ansi-red-
fg">         </span><span class="ansi-green-fg">return</span>
_read<span class="ansi-blue-fg">(</span>filepath_or_buffer<span
class="ansi-blue-fg">,</span> kwds<span class="ansi-blue-fg">)</span>
<span class="ansi-green-intense-fg ansi-bold">    686</span>
<span class="ansi-green-intense-fg ansi-bold">    687</span>
parser_f<span class="ansi-blue-fg">.</span>__name__ <span class="ansi-
blue-fg">=</span> name
<span class="ansi-green-
fg">/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-
packages/pandas/io/parsers.py</span> in <span class="ansi-cyan-
fg">_read</span><span class="ansi-blue-fg">(filepath_or_buffer,
kwds)</span>
<span class="ansi-green-intense-fg ansi-bold">    455</span>
<span class="ansi-green-intense-fg ansi-bold">    456</span>     <span
class="ansi-red-fg"># Create the parser.</span>
<span class="ansi-green-fg">--&gt; 457</span><span class="ansi-red-
fg">     </span>parser <span class="ansi-blue-fg">=</span>
TextFileReader<span class="ansi-blue-fg">(</span>fp_or_buf<span
class="ansi-blue-fg">,</span> <span class="ansi-blue-
fg">**</span>kwds<span class="ansi-blue-fg">)</span>
<span class="ansi-green-intense-fg ansi-bold">    458</span>
<span class="ansi-green-intense-fg ansi-bold">    459</span>     <span
class="ansi-green-fg">if</span> chunksize <span class="ansi-green-
fg">or</span> iterator<span class="ansi-blue-fg">:</span>
<span class="ansi-green-
fg">/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-
packages/pandas/io/parsers.py</span> in <span class="ansi-cyan-
fg">__init__</span><span class="ansi-blue-fg">(self, f, engine,
**kwds)</span>
<span class="ansi-green-intense-fg ansi-bold">    893</span>
self<span class="ansi-blue-fg">.</span>options<span class="ansi-blue-
fg">[</span><span class="ansi-blue-
fg">&#34;has_index_names&#34;</span><span class="ansi-blue-
fg">]</span> <span class="ansi-blue-fg">=</span> kwds<span
class="ansi-blue-fg">[</span><span class="ansi-blue-
fg">&#34;has_index_names&#34;</span><span class="ansi-blue-
fg">]</span>
<span class="ansi-green-intense-fg ansi-bold">    894</span>
<span class="ansi-green-fg">--&gt; 895</span><span class="ansi-red-
fg">         </span>self<span class="ansi-blue-
fg">.</span>_make_engine<span class="ansi-blue-fg">(</span>self<span
class="ansi-blue-fg">.</span>engine<span class="ansi-blue-fg">)</span>
<span class="ansi-green-intense-fg ansi-bold">    896</span>
<span class="ansi-green-intense-fg ansi-bold">    897</span>     <span
class="ansi-green-fg">def</span> close<span class="ansi-blue-
fg">(</span>self<span class="ansi-blue-fg">)</span><span class="ansi-
blue-fg">:</span>
<span class="ansi-green-
fg">/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-
packages/pandas/io/parsers.py</span> in <span class="ansi-cyan-
fg">_make_engine</span><span class="ansi-blue-fg">(self,
engine)</span>
<span class="ansi-green-intense-fg ansi-bold">   1133</span>     <span
class="ansi-green-fg">def</span> _make_engine<span class="ansi-blue-
fg">(</span>self<span class="ansi-blue-fg">,</span> engine<span
class="ansi-blue-fg">=</span><span class="ansi-blue-
fg">&#34;c&#34;</span><span class="ansi-blue-fg">)</span><span
class="ansi-blue-fg">:</span>
<span class="ansi-green-intense-fg ansi-bold">   1134</span>
<span class="ansi-green-fg">if</span> engine <span class="ansi-blue-
fg">==</span> <span class="ansi-blue-fg">&#34;c&#34;</span><span
class="ansi-blue-fg">:</span>
<span class="ansi-green-fg">-&gt; 1135</span><span class="ansi-red-
fg">             </span>self<span class="ansi-blue-fg">.</span>_engine
<span class="ansi-blue-fg">=</span> CParserWrapper<span class="ansi-
blue-fg">(</span>self<span class="ansi-blue-fg">.</span>f<span
class="ansi-blue-fg">,</span> <span class="ansi-blue-
fg">**</span>self<span class="ansi-blue-fg">.</span>options<span
class="ansi-blue-fg">)</span>
<span class="ansi-green-intense-fg ansi-bold">   1136</span>
<span class="ansi-green-fg">else</span><span class="ansi-blue-
fg">:</span>
<span class="ansi-green-intense-fg ansi-bold">   1137</span>
<span class="ansi-green-fg">if</span> engine <span class="ansi-blue-
fg">==</span> <span class="ansi-blue-fg">&#34;python&#34;</span><span
class="ansi-blue-fg">:</span>
<span class="ansi-green-
fg">/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-
packages/pandas/io/parsers.py</span> in <span class="ansi-cyan-
fg">__init__</span><span class="ansi-blue-fg">(self, src,
**kwds)</span>
<span class="ansi-green-intense-fg ansi-bold">   1904</span>
kwds<span class="ansi-blue-fg">[</span><span class="ansi-blue-
fg">&#34;usecols&#34;</span><span class="ansi-blue-fg">]</span> <span
class="ansi-blue-fg">=</span> self<span class="ansi-blue-
fg">.</span>usecols
<span class="ansi-green-intense-fg ansi-bold">   1905</span>
<span class="ansi-green-fg">-&gt; 1906</span><span class="ansi-red-
fg">         </span>self<span class="ansi-blue-fg">.</span>_reader
<span class="ansi-blue-fg">=</span> parsers<span class="ansi-blue-
fg">.</span>TextReader<span class="ansi-blue-fg">(</span>src<span
class="ansi-blue-fg">,</span> <span class="ansi-blue-
fg">**</span>kwds<span class="ansi-blue-fg">)</span>
<span class="ansi-green-intense-fg ansi-bold">   1907</span>
self<span class="ansi-blue-fg">.</span>unnamed_cols <span class="ansi-
blue-fg">=</span> self<span class="ansi-blue-fg">.</span>_reader<span
class="ansi-blue-fg">.</span>unnamed_cols
<span class="ansi-green-intense-fg ansi-bold">   1908</span>
<span class="ansi-green-fg">pandas/_libs/parsers.pyx</span> in <span
class="ansi-cyan-
fg">pandas._libs.parsers.TextReader.__cinit__</span><span class="ansi-
blue-fg">()</span>
<span class="ansi-green-fg">pandas/_libs/parsers.pyx</span> in <span
class="ansi-cyan-
fg">pandas._libs.parsers.TextReader._setup_parser_source</span><span
class="ansi-blue-fg">()</span>
<span class="ansi-red-fg">FileNotFoundError</span>: [Errno 2] File
b&#39;data/countyregions.csv&#39; does not exist:
b&#39;data/countyregions.csv&#39;
</pre></div>

<p>The datasets are missing data; the medians sometimes not defined for a
tract.  For now we won't use columns without data and later go back
and deal with nans using perhaps <code>DataFrame.fillna()</code>.  To start we'll
limit our analysis to communnities of interest defined by race and
ethnicity.  </p>

<div class="highlight"><pre><span></span><span class="k">print</span><span class="p">(</span><span class="s1">&#39;The following columns have nan elements&#39;</span><span class="p">)</span>
<span class="k">print</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">badcol</span><span class="p">))</span>
</pre></div>

<div class="highlight"><pre>
The following columns have nan elements
[&#39;med_age&#39;, &#39;med_fam_in&#39;, &#39;med_g_rent&#39;,
&#39;avghhsize&#39;, &#39;med_hm_val&#39;, &#39;med_c_rent&#39;,
&#39;med_hh_inc&#39;, &#39;med_yr_blt&#39;, &#39;per_cap_in&#39;]
</pre></div>

<h3>Generating District Maps</h3>
<h4>Max-p</h4>
<p>First we'd like to answer the question "Where are the communities?"
The <code>max-p</code> algorithm divides a set of areas into regions with similar
characteristics.  The number of regions is not set, but is chosen by
the algorithm to optimize intra-region similarity.  It does require a
minimum value for each region, in this case we'll say that each region
requires at least 250,000 people, about 5% of the state.  </p>
<p>The maxp algorithm takes some time with the 1250 census tracts.<br />
We'll only do it if asked or if there's no prior saved file. </p>

<div class="highlight"><pre><span></span><span class="n">new_maxp</span> <span class="o">=</span> <span class="bp">False</span>

<span class="k">if</span> <span class="n">new_maxp</span> <span class="o">==</span> <span class="bp">True</span> <span class="ow">or</span> <span class="s1">&#39;maxp&#39;</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">regdat</span><span class="p">[</span><span class="n">currdat</span><span class="p">]</span><span class="o">.</span><span class="n">columns</span><span class="p">:</span>

   <span class="k">print</span><span class="p">(</span><span class="s2">&quot;Beginning maxp regionalization of &quot;</span><span class="o">+</span><span class="n">currdat</span><span class="o">+</span> <span class="s2">&quot;...&quot;</span><span class="p">)</span>
   <span class="n">maxp</span> <span class="o">=</span> <span class="n">region</span><span class="o">.</span><span class="n">max_p_regions</span><span class="o">.</span><span class="n">heuristics</span><span class="o">.</span><span class="n">MaxPRegionsHeu</span><span class="p">()</span>
   <span class="n">maxp</span><span class="o">.</span><span class="n">fit_from_geodataframe</span><span class="p">(</span><span class="n">geodata</span><span class="p">[</span><span class="n">currdat</span><span class="p">],</span> <span class="n">racecat</span><span class="p">,</span>
                              <span class="s1">&#39;population&#39;</span><span class="p">,</span> <span class="mi">500000</span><span class="p">,</span> <span class="n">contiguity</span> <span class="o">=</span> <span class="s1">&#39;queen&#39;</span><span class="p">)</span>
   <span class="k">print</span><span class="p">(</span><span class="s2">&quot;... done.&quot;</span><span class="p">)</span>

   <span class="n">geodata</span><span class="p">[</span><span class="n">currdat</span><span class="p">]</span><span class="o">=</span> <span class="n">geodata</span><span class="p">[</span><span class="n">currdat</span><span class="p">]</span><span class="o">.</span><span class="n">assign</span><span class="p">(</span><span class="n">reg_maxp</span> <span class="o">=</span> <span class="n">maxp</span><span class="o">.</span><span class="n">labels_</span><span class="p">)</span>
   
   <span class="n">geodata</span><span class="p">[</span><span class="n">currdat</span><span class="p">]</span><span class="o">.</span><span class="n">to_file</span><span class="p">(</span><span class="s1">&#39;data/&#39;</span><span class="o">+</span><span class="n">currdat</span><span class="o">+</span><span class="s1">&#39;.geojson&#39;</span><span class="p">,</span> <span class="n">driver</span> <span class="o">=</span> <span class="s1">&#39;GeoJSON&#39;</span><span class="p">)</span>


<span class="n">f</span> <span class="o">=</span> <span class="p">[]</span>
<span class="n">ax</span> <span class="o">=</span> <span class="p">[]</span>

<span class="n">f</span><span class="p">[</span><span class="nb">len</span><span class="p">(</span><span class="n">f</span><span class="p">):],</span> <span class="n">ax</span><span class="p">[</span><span class="nb">len</span><span class="p">(</span><span class="n">ax</span><span class="p">):]</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">(</span><span class="nb">zip</span><span class="p">(</span>  <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">9</span><span class="p">,</span> <span class="mi">9</span><span class="p">))</span>  <span class="p">))</span>
<span class="n">geodata</span><span class="p">[</span><span class="n">currdat</span><span class="p">]</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">column</span><span class="o">=</span><span class="s1">&#39;reg_maxp&#39;</span><span class="p">,</span>
                      <span class="n">categorical</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span>
                      <span class="n">linewidth</span><span class="o">=</span><span class="mf">0.1</span><span class="p">,</span>
                      <span class="n">edgecolor</span><span class="o">=</span><span class="s1">&#39;white&#39;</span><span class="p">,</span>
                      <span class="n">ax</span><span class="o">=</span><span class="n">ax</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">])</span>
<span class="n">ax</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">set_axis_off</span><span class="p">()</span>
</pre></div>

<div class="highlight"><pre>
<span class="ansi-red-
fg">---------------------------------------------------------------------------</span><span
class="ansi-red-fg">NameError</span>
Traceback (most recent call last)<span class="ansi-green-
fg">&lt;ipython-input-1-e4093d4dfca6&gt;</span> in <span class="ansi-
cyan-fg">&lt;module&gt;</span>
<span class="ansi-green-intense-fg ansi-bold">      1</span> new_maxp
<span class="ansi-blue-fg">=</span> <span class="ansi-green-
fg">False</span>
<span class="ansi-green-intense-fg ansi-bold">      2</span>
<span class="ansi-green-fg">----&gt; 3</span><span class="ansi-red-
fg"> </span><span class="ansi-green-fg">if</span> new_maxp <span
class="ansi-blue-fg">==</span> <span class="ansi-green-fg">True</span>
<span class="ansi-green-fg">or</span> <span class="ansi-blue-
fg">&#39;maxp&#39;</span> <span class="ansi-green-fg">not</span> <span
class="ansi-green-fg">in</span> regdat<span class="ansi-blue-
fg">[</span>currdat<span class="ansi-blue-fg">]</span><span
class="ansi-blue-fg">.</span>columns<span class="ansi-blue-
fg">:</span>
<span class="ansi-green-intense-fg ansi-bold">      4</span>
<span class="ansi-green-intense-fg ansi-bold">      5</span>
print<span class="ansi-blue-fg">(</span><span class="ansi-blue-
fg">&#34;Beginning maxp regionalization of &#34;</span><span
class="ansi-blue-fg">+</span>currdat<span class="ansi-blue-
fg">+</span> <span class="ansi-blue-fg">&#34;...&#34;</span><span
class="ansi-blue-fg">)</span>
<span class="ansi-red-fg">NameError</span>: name &#39;regdat&#39; is
not defined
</pre></div>

<p>Of course these cannot be congressional districts.  There must be only
7 districts, one for each seat Colorado has in the House of
Representatives.  </p>

<div class="highlight"><pre><span></span><span class="n">f</span><span class="p">[</span><span class="nb">len</span><span class="p">(</span><span class="n">f</span><span class="p">):],</span> <span class="n">ax</span><span class="p">[</span><span class="nb">len</span><span class="p">(</span><span class="n">ax</span><span class="p">):]</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">(</span><span class="nb">zip</span><span class="p">(</span>  <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">9</span><span class="p">,</span> <span class="mi">9</span><span class="p">))</span>  <span class="p">))</span>
<span class="n">geodata</span><span class="p">[</span><span class="s1">&#39;districts&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">column</span><span class="o">=</span><span class="s1">&#39;emp&#39;</span><span class="p">,</span>
                      <span class="n">categorical</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span>
                      <span class="n">linewidth</span><span class="o">=</span><span class="mf">0.1</span><span class="p">,</span>
                      <span class="n">edgecolor</span><span class="o">=</span><span class="s1">&#39;white&#39;</span><span class="p">,</span>
                      <span class="n">ax</span><span class="o">=</span><span class="n">ax</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">])</span>
<span class="n">ax</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">set_axis_off</span><span class="p">()</span>
</pre></div>

<div class="highlight"><pre>
<span class="ansi-red-
fg">---------------------------------------------------------------------------</span><span
class="ansi-red-fg">NameError</span>
Traceback (most recent call last)<span class="ansi-green-
fg">&lt;ipython-input-1-59f97773d487&gt;</span> in <span class="ansi-
cyan-fg">&lt;module&gt;</span>
<span class="ansi-green-fg">----&gt; 1</span><span class="ansi-red-
fg"> </span>f<span class="ansi-blue-fg">[</span>len<span class="ansi-
blue-fg">(</span>f<span class="ansi-blue-fg">)</span><span
class="ansi-blue-fg">:</span><span class="ansi-blue-fg">]</span><span
class="ansi-blue-fg">,</span> ax<span class="ansi-blue-
fg">[</span>len<span class="ansi-blue-fg">(</span>ax<span class="ansi-
blue-fg">)</span><span class="ansi-blue-fg">:</span><span class="ansi-
blue-fg">]</span> <span class="ansi-blue-fg">=</span> tuple<span
class="ansi-blue-fg">(</span>zip<span class="ansi-blue-fg">(</span>
plt<span class="ansi-blue-fg">.</span>subplots<span class="ansi-blue-
fg">(</span><span class="ansi-cyan-fg">1</span><span class="ansi-blue-
fg">,</span> figsize<span class="ansi-blue-fg">=</span><span
class="ansi-blue-fg">(</span><span class="ansi-cyan-fg">9</span><span
class="ansi-blue-fg">,</span> <span class="ansi-cyan-fg">9</span><span
class="ansi-blue-fg">)</span><span class="ansi-blue-fg">)</span>
<span class="ansi-blue-fg">)</span><span class="ansi-blue-fg">)</span>
<span class="ansi-green-intense-fg ansi-bold">      2</span>
geodata[&#39;districts&#39;].plot(column=&#39;emp&#39;,
<span class="ansi-green-intense-fg ansi-bold">      3</span>
categorical<span class="ansi-blue-fg">=</span><span class="ansi-green-
fg">True</span><span class="ansi-blue-fg">,</span>
<span class="ansi-green-intense-fg ansi-bold">      4</span>
linewidth<span class="ansi-blue-fg">=</span><span class="ansi-cyan-
fg">0.1</span><span class="ansi-blue-fg">,</span>
<span class="ansi-green-intense-fg ansi-bold">      5</span>
edgecolor<span class="ansi-blue-fg">=</span><span class="ansi-blue-
fg">&#39;white&#39;</span><span class="ansi-blue-fg">,</span>
<span class="ansi-red-fg">NameError</span>: name &#39;f&#39; is not
defined
</pre></div>
<img src="data:image/png;base64,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hgR8AAAAAABoSMAHAAAAAICGBHwAAAAAAGhIwAcAAAAAgIYEfAAAAAAAaEjABwAAAACAhgR8AAAAAABoSMAHAAAAAICGBHwAAAAAAGhIwAcAAAAAgIYEfAAAAAAAaEjABwAAAACAhgR8AAAAAABoSMAHAAAAAICGBHwAAAAAAGhIwAcAAAAAgIYEfAAAAAAAaEjABwAAAACAhgR8AAAAAABoSMAHAAAAAICGBHwAAAAAAGhIwAcAAAAAgIYEfAAAAAAAaEjABwAAAACAhgR8AAAAAABoSMAHAAAAAICGBHwAAAAAAGhIwAcAAAAAgIYEfAAAAAAAaEjABwAAAACAhgR8AAAAAABoSMAHAAAAAICGBHwAAAAAAGhIwAcAAAAAgIYEfAAAAAAAaEjABwAAAACAhgR8AAAAAABoSMAHAAAAAICGBHwAAAAAAGhIwAcAAAAAgIYEfAAAAAAAaEjABwAAAACAhgR8AAAAAABoSMAHAAAAAICGBHwAAAAAAGhIwAcAAAAAgIYEfAAAAAAAaEjABwAAAACAhgR8AAAAAABoSMAHAAAAAICGBHwAAAAAAGhIwAcAAAAAgIYEfAAAAAAAaEjABwAAAACAhgR8AAAAAABoSMAHAAAAAICGBHwAAAAAAGhIwAcAAAAAgIYEfAAAAAAAaEjABwAAAACAhgR8AAAAAABoSMAHAAAAAICGBHwAAAAAAGhIwAcAAAAAgIYEfAAAAAAAaEjABwAAAACAhgR8AAAAAABoSMAHAAAAAICGBHwAAAAAAGhIwAcAAAAAgIYEfAAAAAAAaEjABwAAAACAhgR8AAAAAABoSMAHAAAAAICGBHwAAAAAAGhIwAcAAAAAgIYEfAAAAAAAaEjABwAAAACAhgR8AAAAAABoSMAHAAAAAICGBHwAAAAAAGhIwAcAAAAAgIYEfAAAAAAAaEjABwAAAACAhgR8AAAAAABoSMAHAAAAAICGBHwAAAAAAGhIwAcAAAAAgIYEfAAAAAAAaEjABwAAAACAhgR8AAAAAABoSMAHAAAAAICGBHwAAAAAAGhIwAcAAAAAgIYEfAAAAAAAaEjABwAAAACAhgR8AAAAAABoSMAHAAAAAICGBHwAAAAAAGhIwAcAAAAAgIYEfAAAAAAAaEjABwAAAACAhgR8AAAAAABoSMAHAAAAAICGBHwAAAAAAGhIwAcAAAAA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AAAAAKAhAR8AAAAAABoS8AEAAAAAoCEBHwAAAAAAGhLwAQAAAACgIQEfAAAAAAAaEvABAAAAAKAhAR8AAAAAABoS8AEAAAAAoCEBHwAAAAAAGhLwAQAAAACgIQEfAAAAAAAaEvABAAAAAKAhAR8AAAAAABoS8AEAAAAAoCEBHwAAAAAAGhLwAQAAAACgIQEfAAAAAAAaEvABAAAAAKAhAR8AAAAAABoS8AEAAAAAoCEBHwAAAAAAGhLwAQAAAACgIQEfAAAAAAAaEvABAAAAAKAhAR8AAAAAABoS8AEAAAAAoCEBHwAAAAAAGhLwAQAAAACgIQEfAAAAAAAaEvABAAAAAKAhAR8AAAAAABoS8AEAAAAAoCEBHwAAAAAAGhLwAQAAAACgIQEfAAAAAAAaEvABAAAAAKAhAR8AAAAAABoS8AEAAAAAoCEBHwAAAAAAGhLwAQAAAACgIQEfAAAAAAAaEvABAAAAAKAhAR8AAAAAABoS8AEAAAAAoCEBHwAAAAAAGhLwAQAAAACgIQEfAAAAAAAaEvABAAAAAKAhAR8AAAAAABoS8AEAAAAAoCEBHwAAAAAAGhLwAQAAAACgIQEfAAAAAAAaEvABAAAAAKAhAR8AAAAAABoS8AEAAAAAoCEBHwAAAAAAGhLwAQAAAACgIQEfAAAAAAAaEvABAAAAAKAhAR8AAAAAABoS8AEAAAAAoCEBHwAAAAAAGhLwAQAAAACgIQEfAAAAAAAaEvABAAAAAKAhAR8AAAAAABoS8AEAAAAAoCEBHwAAAAAAGhLwAQAAAACgIQEfAAAAAAAaEvABAAAAAKAhAR8AAAAAABoS8AEAAAAAoCEBHwAAAAAAGhLwAQAAAACgIQEfAAAAAAAaEvABAAAAAKAhAR8AAAAAABoS8AEAAAAAoCEBHwAAAAAAGhLwAQAAAACgIQEfAAAAAAAaEvABAAAAAKAhAR8AAAAAABoS8AEAAAAAoCEBHwAAAAAAGhLwAQAAAACgIQEfAAAAAAAaEvABAAAAAKAhAR8AAAAAABoS8AEAAAAAoCEBHwAAAAAAGhLwAQAAAACgIQEfAAAAAAAaEvABAAAAAKAhAR8AAAAAABoS8AEAAAAAoCEBHwAAAAAAGhLwAQAAAACgIQEfAAAAAAAaEvABAAAAAKAhAR8AAAAAABoS8AEAAAAAoCEBHwAAAAAAGhLw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AIUEfAAAAAAAKCTgAwAAAABAIQEfAAAAAAAKCfgAAAAAAFBIwAcAAAAAgEICPgAAAAAAFBLwAQAAAACgkIAPAAAAAACFBHwAAAAAACgk4AMAAAAAQCEBHwAAAAAACgn4AAAAAABQSMAHAAAAAIBCAj4AAAAAABQS8AEAAAAAoJCADwAAAAAAhQR8AAAAAAAoJOADAAAAAEAhAR8AAAAAAAoJ+AAAAAAAUEjABwAAAACAQgI+AAAAAAAUEvABAAAAAKCQgA8AAAAAAIUEfAAAAAAAKCTgAwAAAABAIQEfAAAAAAAKCfgAAAAAAFBIwAcAAAAAgEICPgAAAAAAFBLwAQAAAACgkIAPAAAAAACFBHwAAAAAACgk4AMAAAAAQCEBHwAAAAAACgn4AAAAAABQSMAHAAAAAIBCAj4AAAAAABQS8AEAAAAAoJCADwAAAAAAhQR8AAAAAAAoJOADAAAAAEAhAR8AAAAAAAoJ+AAAAAAAUEjABwAAAACAQgI+AAAAAAAUEvABAAAAAKCQgA8AAAAAAIUEfAAAAAAAKCTgAwAAAABAIQEfAAAAAAAKCfgAAAAAAFBIwAcAAAAAgEICPgAAAAAAFBLwAQAAAACgkIAPAAAAAACFBHwAAAAAACgk4AMAAAAAQCEBHwAAAAAACgn4AAAAAABQSMAHAAAAAIBCAj4AAAAAABQS8AEAAAAAoJCADwAAAAAAhQR8AAAAAAAoJOADAAAAAEAhAR8AAAAAAAoJ+AAAAAAAUEjABwAAAACAQgI+AAAAAAAUEvABAAAAAKCQgA8AAAAAAIUEfAAAAAAAKCTgAwAAAABAIQEfAAAAAAAKCfgAAAAAAFBIwAcAAAAAgEICPgAAAAAAFBLwAQAAAACgkIAPAAAAAACFBHwAAAAAACgk4AMAAAAAQCEBHwAAAAAACgn4AAAAAABQSMAHAAAAAIBCAj4AAAAAABQS8AEAAAAAoJCADwAAAAAAhQR8AAAAAAAoJOADAAAAAEAhAR8AAAAAAAoJ+AAAAAAAUEjABwAAAACAQgI+AAAAAAAUEvABAAAAAKCQgA8AAAAAAIUEfAAAAAAAKCTgAwAAAABAIQEfAAAAAAAKCfgAAAAAAFBIwAcAAAAAgEICPgAAAAAAFBLwAQAAAACgkIAPAAAAAACFBHwAAAAAACgk4AMAAAAAQCEBHwAAAAAACgn4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AAAAAABQSMAHAAAAAIBCAj4AAAAAABQS8AEAAAAAoJCADwAAAAAAhQR8AAAAAAAoJOADAAAAAEAhAR8AAAAAAAoJ+AAAAAAAUEjABwAAAACAQgI+AAAAAAAUEvABAAAAAKCQgA8AAAAAAIUEfAAAAAAAKCTgAwAAAABAIQEfAAAAAAAKCfgAAAAAAFBIwAcAAAAAgEICPgAAAAAAFBLwAQAAAACgkIAPAAAAAACFBHwAAAAAACgk4AMAAAAAQCEBHwAAAAAACgn4AAAAAABQSMAHAAAAAIBCAj4AAAAAABQS8AEAAAAAoJCADwAAAAAAhQR8AAAAAAAoJOADAAAAAEAhAR8AAAAAAAoJ+AAAAAAAUEjABwAAAACAQgI+AAAAAAAUEvABAAAAAKCQgA8AAAAAAIUEfAAAAAAAKCTgAwAAAABAIQEfAAAAAAAKCfgAAAAAAFBIwAcAAAAAgEICPgAAAAAAFBLwAQAAAACgkIAPAAAAAACFBHwAAAAAACgk4AMAAAAAQCEBHwAAAAAACgn4AAAAAABQSMAHAAAAAIBCAj4AAAAAABQS8AEAAAAAoJCADwAAAAAAhQR8AAAAAAAoJOADAAAAAEAhAR8AAAAAAAoJ+AAAAAAAUEjABwAAAACAQgI+AAAAAAAUEvABAAAAAKCQgA8AAAAAAIUEfAAAAAAAKCTgAwAAAABAIQEfAAAAAAAKCfgAAAAAAFBIwAcAAAAAgEICPgAAAAAAFBLwAQAAAACgkIAPAAAAAACFBHwAAAAAACgk4AMAAAAAQCEBHwAAAAAACgn4AAAAAABQSMAHAAAAAIBCAj4AAAAAABQS8AEAAAAAoJCADwAAAAAAhQR8AAAAAAAoJOADAAAAAEAhAR8AAAAAAAoJ+AAAAAAAUEjABwAAAACAQgI+AAAAAAAUEvABAAAAAKCQgA8AAAAAAIUEfAAAAAAAKCTgAwAAAABAIQEfAAAAAAAKCfgAAAAAAFBIwAcAAAAAgEICPgAAAAAAFBLwAQAAAACgkIAPAAAAAACFBHwAAAAAACgk4AMAAAAAQCEBHwAAAAAACgn4AAAAAABQSMAHAAAAAIBCAj4AAAAAABQS8AEAAAAAoJCADwAAAAAAhQR8AAAAAAAoJOADAAAAAEAhAR8AAAAAAAoJ+AAAAAAAUEjABwAAAACAQgI+AAAAAAAUEvABAAAA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OiTABwAAAACADgnwAQAAAACgQwJ8AAAAAADokAAfAAAAAAA6JMAHAAAAAIAOCfABAAAAAKBDAnwAAAAAAOiQAB8AAAAAADokwAcAAAAAgA4J8AEAAAAAoEMCfAAAAAAA6JAAHwAAAAAAOiTABwAAAACADgnwAQAAAACgQwJ8AAAAAADokAAfAAAAAAA6JMAHAAAAAIAOCfABAAAAAKBDAnwAAAAAAOiQAB8AAAAAADokwAcAAAAAgA4J8AEAAAAAoEMCfAAAAAAA6JAAHwAAAAAAOiTABwAAAACADgnwAQAAAACgQwJ8AAAAAADokAAfAAAAAAA6JMAHAAAAAIAOCfABAAAAAKBDAnwAAAAAAOiQAB8AAAAAADokwAcAAAAAgA4J8AEAAAAAoEMCfAAAAAAA6JAAHwAAAAAAOiTABwAAAACADgnwAQAAAACgQwJ8AAAAAADokAAfAAAAAAA6JMAHAAAAAIAOCfABAAAAAKBDAnwAAAAAAOiQAB8AAAAAADokwAcAAAAAgA4J8AEAAAAAoEMCfAAAAAAA6JAAHwAAAAAAOiTABwAAAACADgnwAQAAAACgQwJ8AAAAAADokAAfAAAAAAA6JMAHAAAAAIAOCfABAAAAAKBDAnwAAAAAAOiQAB8AAAAAADokwAcAAAAAgA4J8AEAAAAAoEMCfAAAAAAA6JAAHwAAAAAAOiTABwAAAACADgnwAQAAAACgQwJ8AAAAAADokAAfAAAAAAA6JMAHAAAAAIAOCfABAAAAAKBDAnwAAAAAAOiQAB8AAAAAADokwAcAAAAAgA4J8AEAAAAAoEMCfAAAAAAA6JAAHwAAAAAAOiTABwAAAACADgnwAQAAAACgQwJ8AAAAAADokAAfAAAAAAA6JMAHAAAAAIAOCfABAAAAAKBDAnwAAAAAAOiQAB8AAAAAADokwAcAAAAAgA4J8AEAAAAAoEMCfAAAAAAA6JAAHwAAAAAAOiTABwAAAACADgnwAQAAAACgQwJ8AAAAAADokAAfAAAAAAA6JMAHAAAAAIAOCfABAAAAAKBDAnwAAAAAAOiQAB8AAAAAADokwAcAAAAAgA4J8AEAAAAAoEMCfAAAAAAA6JAAHwAAAAAAOiTABwAAAACADgnwAQAAAACgQwJ8AAAAAADokAAfAAAAAAA6JMAHAAAAAIAOCfABAAAAAKBDAnwAAAAA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" width="600"/>

<h4>Demographic Data Only</h4>
<p>Now we will use the AZP algorithm to generate a specific number of
districts.  The algorithm optimizes an objective function, which in
this case includes intra-region similarity and total population.
Let's have a look at the output of the AZP regionalization of
Colorado's census tracts.</p>
<p>The AZP algorithm also takes some time with the 1250 census tracts.
The exact versions of these problems are np hard, and even the
heuristic takes a while.  Again we'll only do it if asked or if there
is no prior saved file.</p>

<div class="highlight"><pre><span></span><span class="n">new_azp</span>  <span class="o">=</span> <span class="bp">False</span>
<span class="k">if</span> <span class="n">new_azp</span> <span class="o">==</span> <span class="bp">True</span> <span class="ow">or</span> <span class="s1">&#39;pair&#39;</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">regdat</span><span class="p">[</span><span class="n">currdat</span><span class="p">]</span><span class="o">.</span><span class="n">columns</span><span class="p">:</span>

    <span class="n">pregazp</span> <span class="o">=</span> <span class="n">region</span><span class="o">.</span><span class="n">p_regions</span><span class="o">.</span><span class="n">azp</span><span class="o">.</span><span class="n">AZP</span><span class="p">()</span>
    <span class="k">print</span><span class="p">(</span><span class="s2">&quot;Beginning AZP regionalization of &quot;</span><span class="o">+</span><span class="n">currdat</span><span class="o">+</span> <span class="s2">&quot;...&quot;</span><span class="p">)</span>
 
    <span class="n">pregazp</span><span class="o">.</span><span class="n">fit_from_geodataframe</span><span class="p">(</span><span class="n">geodata</span><span class="p">[</span><span class="n">currdat</span><span class="p">],</span> <span class="n">racecat</span><span class="p">,</span> 
                                  <span class="n">ndist</span><span class="p">,</span> <span class="n">contiguity</span> <span class="o">=</span> <span class="s2">&quot;queen&quot;</span><span class="p">,</span> 
                                  <span class="n">objective_func</span> <span class="o">=</span> <span class="n">ObjectiveFunctionPairwise</span><span class="p">()</span>
                                  <span class="p">)</span>
    <span class="k">print</span><span class="p">(</span><span class="s2">&quot;... done.&quot;</span><span class="p">)</span>
    
    <span class="n">regdat</span><span class="p">[</span><span class="n">currdat</span><span class="p">]</span> <span class="o">=</span> <span class="n">regdat</span><span class="p">[</span><span class="n">currdat</span><span class="p">]</span><span class="o">.</span><span class="n">assign</span><span class="p">(</span><span class="n">pair</span> <span class="o">=</span> <span class="n">pregazp</span><span class="o">.</span><span class="n">labels_</span><span class="p">)</span>
    <span class="n">regdat</span><span class="p">[</span><span class="n">currdat</span><span class="p">]</span><span class="o">.</span><span class="n">to_csv</span><span class="p">(</span><span class="s1">&#39;data/&#39;</span><span class="o">+</span><span class="n">currdat</span><span class="o">+</span><span class="s1">&#39;regions.csv&#39;</span><span class="p">,</span> <span class="n">index</span> <span class="o">=</span> <span class="bp">False</span><span class="p">)</span>

<span class="n">f</span><span class="p">[</span><span class="nb">len</span><span class="p">(</span><span class="n">f</span><span class="p">):],</span> <span class="n">ax</span><span class="p">[</span><span class="nb">len</span><span class="p">(</span><span class="n">ax</span><span class="p">):]</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">(</span><span class="nb">zip</span><span class="p">(</span>  <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">9</span><span class="p">,</span> <span class="mi">9</span><span class="p">))</span>  <span class="p">))</span>
<span class="n">geodata</span><span class="p">[</span><span class="n">currdat</span><span class="p">]</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">column</span><span class="o">=</span><span class="s1">&#39;reg_azp&#39;</span><span class="p">,</span>
                      <span class="n">categorical</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span>
                      <span class="n">linewidth</span><span class="o">=</span><span class="mf">0.1</span><span class="p">,</span>
                      <span class="n">edgecolor</span><span class="o">=</span><span class="s1">&#39;white&#39;</span><span class="p">,</span>
                      <span class="n">ax</span><span class="o">=</span><span class="n">ax</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">])</span>
<span class="n">ax</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">set_axis_off</span><span class="p">()</span>


<span class="n">regpops</span> <span class="o">=</span> <span class="n">getpop</span><span class="p">(</span><span class="s1">&#39;population&#39;</span><span class="p">)</span>
<span class="n">distpop</span> <span class="o">=</span> <span class="nb">sum</span><span class="p">(</span><span class="n">geodata</span><span class="p">[</span><span class="n">currdat</span><span class="p">]</span><span class="o">.</span><span class="n">population</span><span class="p">)</span> <span class="o">/</span> <span class="mi">7</span>
</pre></div>

<div class="highlight"><pre>
<span class="ansi-red-
fg">---------------------------------------------------------------------------</span><span
class="ansi-red-fg">NameError</span>
Traceback (most recent call last)<span class="ansi-green-
fg">&lt;ipython-input-1-3590a4b24bc1&gt;</span> in <span class="ansi-
cyan-fg">&lt;module&gt;</span>
<span class="ansi-green-intense-fg ansi-bold">      1</span> new_azp
<span class="ansi-blue-fg">=</span> <span class="ansi-green-
fg">False</span>
<span class="ansi-green-fg">----&gt; 2</span><span class="ansi-red-
fg"> </span><span class="ansi-green-fg">if</span> new_azp <span
class="ansi-blue-fg">==</span> <span class="ansi-green-fg">True</span>
<span class="ansi-green-fg">or</span> <span class="ansi-blue-
fg">&#39;pair&#39;</span> <span class="ansi-green-fg">not</span> <span
class="ansi-green-fg">in</span> regdat<span class="ansi-blue-
fg">[</span>currdat<span class="ansi-blue-fg">]</span><span
class="ansi-blue-fg">.</span>columns<span class="ansi-blue-
fg">:</span>
<span class="ansi-green-intense-fg ansi-bold">      3</span>
<span class="ansi-green-intense-fg ansi-bold">      4</span>
pregazp <span class="ansi-blue-fg">=</span> region<span class="ansi-
blue-fg">.</span>p_regions<span class="ansi-blue-fg">.</span>azp<span
class="ansi-blue-fg">.</span>AZP<span class="ansi-blue-
fg">(</span><span class="ansi-blue-fg">)</span>
<span class="ansi-green-intense-fg ansi-bold">      5</span>
print<span class="ansi-blue-fg">(</span><span class="ansi-blue-
fg">&#34;Beginning AZP regionalization of &#34;</span><span
class="ansi-blue-fg">+</span>currdat<span class="ansi-blue-
fg">+</span> <span class="ansi-blue-fg">&#34;...&#34;</span><span
class="ansi-blue-fg">)</span>
<span class="ansi-red-fg">NameError</span>: name &#39;regdat&#39; is
not defined
</pre></div>

<p>These districts obviously show no regard for other criteria of
good congressional districts, like compactness, overlap with current
districts (below) or respect for natural features like mountains.
These could be included in the analysis by editing the objective
function.  In <code>helpers</code> we provide an objective function that composes
other objective functions.  </p>
<p>There is however, a bigger problem with this choice of regionalization.  The
law provides that each district be equal in population to within 5%.</p>
<blockquote>
<p>FIVE PERCENT DEVIATION TEST means that the sum of (a) the percent by
which the largest district's population exceeds that of the ideal
district and (b) the percent by which the smallest district's
population falls short of the population of the ideal district, must
be less than five percent. In re Reapportionment of
Colo. Gen. Ass'y, 647 P.2d 191 (Colo. 1982).
In this case that means the population of each district must be close
to ---------------------------------------------------------------------------NameError                                 Traceback (most recent call last)<ipython-input-1-6806066033f7> in <module>
----&gt; 1 distpop
NameError: name 'distpop' is not defined.  Since we don't include it in the objective function
our districts do not fillow this:</p>
</blockquote>

<div class="highlight"><pre><span></span><span class="k">print</span><span class="p">(</span><span class="s1">&#39;The largest district is {0:2.0f}% above average&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">((</span><span class="nb">max</span><span class="p">(</span><span class="n">regpops</span><span class="p">)</span><span class="o">/</span><span class="n">distpop</span> <span class="o">-</span><span class="mi">1</span><span class="p">)</span><span class="o">*</span><span class="mi">100</span><span class="p">))</span>
<span class="k">print</span><span class="p">(</span><span class="s1">&#39;The smallest district is {0:2.0f}% below average&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">((</span><span class="mi">1</span> <span class="o">-</span> <span class="nb">min</span><span class="p">(</span><span class="n">regpops</span><span class="p">)</span><span class="o">/</span><span class="n">distpop</span><span class="p">)</span><span class="o">*</span><span class="mi">100</span><span class="p">))</span>
</pre></div>

<div class="highlight"><pre>
<span class="ansi-red-
fg">---------------------------------------------------------------------------</span><span
class="ansi-red-fg">NameError</span>
Traceback (most recent call last)<span class="ansi-green-
fg">&lt;ipython-input-1-9f2a6d9c389d&gt;</span> in <span class="ansi-
cyan-fg">&lt;module&gt;</span>
<span class="ansi-green-fg">----&gt; 1</span><span class="ansi-red-
fg"> </span>print<span class="ansi-blue-fg">(</span><span class="ansi-
blue-fg">&#39;The largest district is {0:2.0f}% above
average&#39;</span><span class="ansi-blue-fg">.</span>format<span
class="ansi-blue-fg">(</span><span class="ansi-blue-
fg">(</span>max<span class="ansi-blue-fg">(</span>regpops<span
class="ansi-blue-fg">)</span><span class="ansi-blue-
fg">/</span>distpop <span class="ansi-blue-fg">-</span><span
class="ansi-cyan-fg">1</span><span class="ansi-blue-fg">)</span><span
class="ansi-blue-fg">*</span><span class="ansi-cyan-
fg">100</span><span class="ansi-blue-fg">)</span><span class="ansi-
blue-fg">)</span>
<span class="ansi-green-intense-fg ansi-bold">      2</span>
print<span class="ansi-blue-fg">(</span><span class="ansi-blue-
fg">&#39;The smallest district is {0:2.0f}% below
average&#39;</span><span class="ansi-blue-fg">.</span>format<span
class="ansi-blue-fg">(</span><span class="ansi-blue-fg">(</span><span
class="ansi-cyan-fg">1</span> <span class="ansi-blue-fg">-</span>
min<span class="ansi-blue-fg">(</span>regpops<span class="ansi-blue-
fg">)</span><span class="ansi-blue-fg">/</span>distpop<span
class="ansi-blue-fg">)</span><span class="ansi-blue-fg">*</span><span
class="ansi-cyan-fg">100</span><span class="ansi-blue-
fg">)</span><span class="ansi-blue-fg">)</span>
<span class="ansi-red-fg">NameError</span>: name &#39;regpops&#39; is
not defined
</pre></div>

<p>Equal populations is part of the goal of the regionalization analysis,
but it isn't included in the objective function.  In a later section
we'll use an objective function class from <code>helpers</code> that can compse
several objectives, including the need to balance population among
districts.</p>
<h4>Including multiple objectives</h4>
<p>There are several objective functions provided by pysal, but there
isn't one that seeks to balance population among regions.  There also
is no way to include several objectives.  I modified pysal's 
<code>objective_function.py</code> to address this.  </p>
<p><code>ObjectiveFunctionBalance</code> is merely the spread between the highest and
lowest total of the attribute.  <code>ObjectiveFunctionComposite</code> takes a
list of other objective functions, passes the same labels but
different attributes, receives the values, and combines them into one
overall result.  </p>
<p>Let's use these functions to generate a map that keeps race-based
communities of interest, but also places equal numbers in each
district.</p>
<p><code>ObjectiveFunctionComposite</code> allows weighting each different
sub-objective. To make values from each sub-objective comensurate,
we'll scale each, by dividing by the <code>natural_weight</code>, a typical value
of the objective function.  </p>

<div class="highlight"><pre><span></span><span class="n">flist</span> <span class="o">=</span> <span class="p">[</span><span class="n">ObjectiveFunctionBalance</span><span class="p">,</span>
         <span class="n">ObjectiveFunctionPairwise</span>
<span class="p">]</span>
<span class="n">attlist</span> <span class="o">=</span> <span class="p">[[</span><span class="s1">&#39;population&#39;</span><span class="p">],</span> <span class="n">racecat</span><span class="p">]</span>

<span class="k">def</span> <span class="nf">make_weight</span><span class="p">(</span><span class="n">functions</span><span class="p">,</span> <span class="n">attributes</span><span class="p">):</span>
    <span class="nb">iter</span> <span class="o">=</span> <span class="p">(</span><span class="mi">1</span><span class="o">/</span>
            <span class="p">(</span><span class="n">f</span><span class="p">()</span><span class="o">.</span><span class="n">natural_weight</span><span class="p">(</span><span class="n">region</span><span class="o">.</span><span class="n">util</span><span class="o">.</span><span class="n">array_from_df_col</span><span class="p">(</span><span class="n">geodata</span><span class="p">[</span><span class="n">currdat</span><span class="p">],</span> <span class="n">at</span><span class="p">)))</span>
            <span class="k">for</span> <span class="p">(</span><span class="n">f</span><span class="p">,</span> <span class="n">at</span><span class="p">)</span>
            <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span><span class="n">functions</span><span class="p">,</span> <span class="n">attributes</span><span class="p">))</span>
    <span class="k">return</span>  <span class="n">np</span><span class="o">.</span><span class="n">fromiter</span><span class="p">(</span><span class="nb">iter</span><span class="p">,</span> <span class="nb">float</span><span class="p">)</span>

<span class="n">w0</span> <span class="o">=</span> <span class="n">make_weight</span><span class="p">(</span><span class="n">flist</span><span class="p">,</span> <span class="n">attlist</span><span class="p">)</span>

<span class="n">new_azp</span>  <span class="o">=</span> <span class="bp">False</span>
<span class="k">if</span> <span class="n">new_azp</span> <span class="o">==</span> <span class="bp">True</span> <span class="ow">or</span> <span class="s1">&#39;pair_bal&#39;</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">regdat</span><span class="p">[</span><span class="n">currdat</span><span class="p">]</span><span class="o">.</span><span class="n">columns</span><span class="p">:</span>
    <span class="n">pregazp</span> <span class="o">=</span> <span class="n">region</span><span class="o">.</span><span class="n">p_regions</span><span class="o">.</span><span class="n">azp</span><span class="o">.</span><span class="n">AZP</span><span class="p">()</span>
    <span class="n">func</span> <span class="o">=</span> <span class="n">ObjectiveFunctionComposite</span><span class="p">(</span><span class="n">flist</span><span class="p">,</span> <span class="n">attlist</span><span class="p">,</span> <span class="n">w0</span><span class="p">)</span>        
    <span class="n">pregazp</span> <span class="o">=</span> <span class="n">region</span><span class="o">.</span><span class="n">p_regions</span><span class="o">.</span><span class="n">azp</span><span class="o">.</span><span class="n">AZP</span><span class="p">()</span>

    <span class="k">print</span><span class="p">(</span><span class="s2">&quot;Beginning AZP regionalization of &quot;</span><span class="o">+</span><span class="n">currdat</span><span class="o">+</span> <span class="s2">&quot;...&quot;</span><span class="p">)</span>
    <span class="n">pregazp</span><span class="o">.</span><span class="n">fit_from_geodataframe</span><span class="p">(</span><span class="n">geodata</span><span class="p">[</span><span class="n">currdat</span><span class="p">],</span>
                                  <span class="n">func</span><span class="o">.</span><span class="n">flat_attr_list</span><span class="p">,</span> 
                                  <span class="n">ndist</span><span class="p">,</span>
                                  <span class="n">contiguity</span> <span class="o">=</span> <span class="s2">&quot;queen&quot;</span><span class="p">,</span> 
                                  <span class="n">objective_func</span> <span class="o">=</span> <span class="n">func</span>
                                  <span class="p">)</span>
    <span class="k">print</span><span class="p">(</span><span class="s2">&quot;... done.&quot;</span><span class="p">)</span>

    <span class="n">regdat</span><span class="p">[</span><span class="n">currdat</span><span class="p">]</span> <span class="o">=</span> <span class="n">regdat</span><span class="p">[</span><span class="n">currdat</span><span class="p">]</span><span class="o">.</span><span class="n">assign</span><span class="p">(</span><span class="n">pair_bal</span> <span class="o">=</span> <span class="n">pregazp</span><span class="o">.</span><span class="n">labels_</span><span class="p">)</span>
    <span class="n">regdat</span><span class="p">[</span><span class="n">currdat</span><span class="p">]</span><span class="o">.</span><span class="n">to_csv</span><span class="p">(</span><span class="s1">&#39;data/&#39;</span><span class="o">+</span><span class="n">currdat</span><span class="o">+</span><span class="s1">&#39;regions.csv&#39;</span><span class="p">,</span> <span class="n">index</span> <span class="o">=</span> <span class="bp">False</span><span class="p">)</span>

<span class="n">f</span><span class="p">[</span><span class="nb">len</span><span class="p">(</span><span class="n">f</span><span class="p">):],</span> <span class="n">ax</span><span class="p">[</span><span class="nb">len</span><span class="p">(</span><span class="n">ax</span><span class="p">):]</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">(</span><span class="nb">zip</span><span class="p">(</span>  <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">9</span><span class="p">,</span> <span class="mi">9</span><span class="p">))</span>  <span class="p">))</span>
<span class="n">geodata</span><span class="p">[</span><span class="n">currdat</span><span class="p">]</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">column</span><span class="o">=</span><span class="s1">&#39;reg_comp&#39;</span><span class="p">,</span>
                      <span class="n">categorical</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span>
                      <span class="n">linewidth</span><span class="o">=</span><span class="mf">0.1</span><span class="p">,</span>
                      <span class="n">edgecolor</span><span class="o">=</span><span class="s1">&#39;white&#39;</span><span class="p">,</span>
                      <span class="n">ax</span><span class="o">=</span><span class="n">ax</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">])</span>
<span class="n">ax</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">set_axis_off</span><span class="p">()</span>
</pre></div>

<div class="highlight"><pre>
<span class="ansi-red-
fg">---------------------------------------------------------------------------</span><span
class="ansi-red-fg">NameError</span>
Traceback (most recent call last)<span class="ansi-green-
fg">&lt;ipython-input-1-2950dbd22a7a&gt;</span> in <span class="ansi-
cyan-fg">&lt;module&gt;</span>
<span class="ansi-green-intense-fg ansi-bold">     14</span>
<span class="ansi-green-intense-fg ansi-bold">     15</span> new_azp
<span class="ansi-blue-fg">=</span> <span class="ansi-green-
fg">False</span>
<span class="ansi-green-fg">---&gt; 16</span><span class="ansi-red-
fg"> </span><span class="ansi-green-fg">if</span> new_azp <span
class="ansi-blue-fg">==</span> <span class="ansi-green-fg">True</span>
<span class="ansi-green-fg">or</span> <span class="ansi-blue-
fg">&#39;pair_bal&#39;</span> <span class="ansi-green-fg">not</span>
<span class="ansi-green-fg">in</span> regdat<span class="ansi-blue-
fg">[</span>currdat<span class="ansi-blue-fg">]</span><span
class="ansi-blue-fg">.</span>columns<span class="ansi-blue-
fg">:</span>
<span class="ansi-green-intense-fg ansi-bold">     17</span>
pregazp <span class="ansi-blue-fg">=</span> region<span class="ansi-
blue-fg">.</span>p_regions<span class="ansi-blue-fg">.</span>azp<span
class="ansi-blue-fg">.</span>AZP<span class="ansi-blue-
fg">(</span><span class="ansi-blue-fg">)</span>
<span class="ansi-green-intense-fg ansi-bold">     18</span>     func
<span class="ansi-blue-fg">=</span> ObjectiveFunctionComposite<span
class="ansi-blue-fg">(</span>flist<span class="ansi-blue-fg">,</span>
attlist<span class="ansi-blue-fg">,</span> w0<span class="ansi-blue-
fg">)</span>
<span class="ansi-red-fg">NameError</span>: name &#39;regdat&#39; is
not defined
</pre></div>

<p>The districts still aren't balanced that well.  The largest district is 
---------------------------------------------------------------------------NameError                                 Traceback (most recent call last)<ipython-input-1-06ee29fd0ed2> in <module>
----&gt; 1 '{0:2.0f}%'.format((max(regpops)/distpop -1) * 100)
NameError: name 'regpops' is not defined 
larger than average, and the smallest is 
---------------------------------------------------------------------------NameError                                 Traceback (most recent call last)<ipython-input-1-76c9c7a5639d> in <module>
----&gt; 1 '{0:2.0f}%'.format((1 - min(regpops)/distpop) * 100)
NameError: name 'regpops' is not defined
smaller.  </p>
<h4>Including compactness</h4>
<p>The districts shown so far are absurd because they snake all around,
just like Gerry's salamander.  Now let's include compactness in the
objective by providing a compactness function that measures perimeter
of the districts.   </p>

<div class="highlight"><pre><span></span><span class="n">flist</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">ObjectiveFunctionCompactness</span><span class="p">)</span>
<span class="n">attlist</span><span class="o">.</span><span class="n">append</span><span class="p">([</span><span class="s1">&#39;geometry&#39;</span><span class="p">])</span>
<span class="n">w0</span> <span class="o">=</span> <span class="n">make_weight</span><span class="p">(</span><span class="n">flist</span><span class="p">,</span> <span class="n">attlist</span><span class="p">)</span>

<span class="k">if</span> <span class="n">new_azp</span> <span class="o">==</span> <span class="bp">True</span> <span class="ow">or</span> <span class="s1">&#39;pair_bal_pact&#39;</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">regdat</span><span class="p">[</span><span class="n">currdat</span><span class="p">]</span><span class="o">.</span><span class="n">columns</span><span class="p">:</span>
    <span class="n">pregazp</span> <span class="o">=</span> <span class="n">region</span><span class="o">.</span><span class="n">p_regions</span><span class="o">.</span><span class="n">azp</span><span class="o">.</span><span class="n">AZP</span><span class="p">()</span>
    <span class="n">func</span> <span class="o">=</span> <span class="n">ObjectiveFunctionComposite</span><span class="p">(</span><span class="n">flist</span><span class="p">,</span> <span class="n">attlist</span><span class="p">,</span> <span class="n">w0</span><span class="p">)</span>

    <span class="n">pregazp</span><span class="o">.</span><span class="n">fit_from_geodataframe</span><span class="p">(</span><span class="n">geodata</span><span class="p">[</span><span class="n">currdat</span><span class="p">],</span>
                                  <span class="n">func</span><span class="o">.</span><span class="n">flat_attr_list</span><span class="p">,</span>
                                  <span class="n">ndist</span><span class="p">,</span>
                                  <span class="n">contiguity</span> <span class="o">=</span> <span class="s1">&#39;queen&#39;</span><span class="p">,</span>
                                  <span class="n">objective_func</span> <span class="o">=</span> <span class="n">func</span>
    <span class="p">)</span>

    <span class="n">regdat</span><span class="p">[</span><span class="n">currdat</span><span class="p">]</span> <span class="o">=</span> <span class="n">regdat</span><span class="p">[</span><span class="n">currdat</span><span class="p">]</span><span class="o">.</span><span class="n">assign</span><span class="p">(</span><span class="n">pair_bal_pact</span> <span class="o">=</span> <span class="n">pregazp</span><span class="o">.</span><span class="n">labels_</span><span class="p">)</span>
    <span class="n">regdat</span><span class="p">[</span><span class="n">currdat</span><span class="p">]</span><span class="o">.</span><span class="n">to_csv</span><span class="p">(</span><span class="s1">&#39;data/&#39;</span><span class="o">+</span><span class="n">currdat</span><span class="o">+</span><span class="s1">&#39;regions.csv&#39;</span><span class="p">,</span> <span class="n">index</span> <span class="o">=</span> <span class="bp">False</span><span class="p">)</span>

<span class="n">f</span><span class="p">[</span><span class="nb">len</span><span class="p">(</span><span class="n">f</span><span class="p">):],</span> <span class="n">ax</span><span class="p">[</span><span class="nb">len</span><span class="p">(</span><span class="n">ax</span><span class="p">):]</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">(</span><span class="nb">zip</span><span class="p">(</span>  <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">9</span><span class="p">,</span> <span class="mi">9</span><span class="p">))</span>  <span class="p">))</span>
<span class="n">g</span><span class="p">[</span><span class="s1">&#39;labels&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">pregazp</span><span class="o">.</span><span class="n">labels_</span>
<span class="n">g</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">column</span><span class="o">=</span><span class="s1">&#39;labels&#39;</span><span class="p">,</span>
       <span class="n">categorical</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span>
       <span class="n">linewidth</span><span class="o">=</span><span class="mf">0.1</span><span class="p">,</span>
       <span class="n">edgecolor</span><span class="o">=</span><span class="s1">&#39;white&#39;</span><span class="p">,</span>
       <span class="n">ax</span><span class="o">=</span><span class="n">ax</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">])</span>
<span class="n">ax</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">set_axis_off</span><span class="p">()</span>

<span class="n">f</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>

<div class="highlight"><pre>
<span class="ansi-red-
fg">---------------------------------------------------------------------------</span><span
class="ansi-red-fg">NameError</span>
Traceback (most recent call last)<span class="ansi-green-
fg">&lt;ipython-input-1-8a95ef7600e4&gt;</span> in <span class="ansi-
cyan-fg">&lt;module&gt;</span>
<span class="ansi-green-intense-fg ansi-bold">      3</span> w0 <span
class="ansi-blue-fg">=</span> make_weight<span class="ansi-blue-
fg">(</span>flist<span class="ansi-blue-fg">,</span> attlist<span
class="ansi-blue-fg">)</span>
<span class="ansi-green-intense-fg ansi-bold">      4</span>
<span class="ansi-green-fg">----&gt; 5</span><span class="ansi-red-
fg"> </span><span class="ansi-green-fg">if</span> new_azp <span
class="ansi-blue-fg">==</span> <span class="ansi-green-fg">True</span>
<span class="ansi-green-fg">or</span> <span class="ansi-blue-
fg">&#39;pair_bal_pact&#39;</span> <span class="ansi-green-
fg">not</span> <span class="ansi-green-fg">in</span> regdat<span
class="ansi-blue-fg">[</span>currdat<span class="ansi-blue-
fg">]</span><span class="ansi-blue-fg">.</span>columns<span
class="ansi-blue-fg">:</span>
<span class="ansi-green-intense-fg ansi-bold">      6</span>
pregazp <span class="ansi-blue-fg">=</span> region<span class="ansi-
blue-fg">.</span>p_regions<span class="ansi-blue-fg">.</span>azp<span
class="ansi-blue-fg">.</span>AZP<span class="ansi-blue-
fg">(</span><span class="ansi-blue-fg">)</span>
<span class="ansi-green-intense-fg ansi-bold">      7</span>     func
<span class="ansi-blue-fg">=</span> ObjectiveFunctionComposite<span
class="ansi-blue-fg">(</span>flist<span class="ansi-blue-fg">,</span>
attlist<span class="ansi-blue-fg">,</span> w0<span class="ansi-blue-
fg">)</span>
<span class="ansi-red-fg">NameError</span>: name &#39;regdat&#39; is
not defined
</pre></div>

<h4>Future Work</h4>
<p>We'll have to better weight the requirement of even populations in
order to have a map that passes muster.  In addition, we have a sense
of how well the regionalization preserves communities of interest, but
could we do better?  At what cost?  To answer that quantitatively, I'd
like to generate a set of random regionalizations and see where our
optimized regionalization ranks, both in variables that were optimized
and those that weren't.  This pseudo-p value will characterize how
different weightings of variables affect the final result.  </p>
    <HR/>
    <div class="footer">
      <p>Published from <a href="Regionalization.pmd">Regionalization.pmd</a>
    using <a href="http://mpastell.com/pweave">Pweave</a> 0.30.3
    on 02-11-2019.<p></div>

            </div>
        </div>
    </div>
  </BODY>
</HTML>
