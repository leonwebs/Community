
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
<h2>Evaluating District Maps</h2>

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
        <span class="n">label</span> <span class="o">=</span> <span class="n">regdat</span><span class="p">[</span><span class="n">currdat</span><span class="p">]</span><span class="o">.</span><span class="n">pair</span>
    <span class="k">return</span> <span class="p">[</span><span class="nb">sum</span><span class="p">([</span><span class="n">gdat</span><span class="p">[</span><span class="n">col</span><span class="p">][</span><span class="n">i</span><span class="p">]</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">np</span><span class="o">.</span><span class="n">where</span><span class="p">(</span><span class="n">label</span> <span class="o">==</span> <span class="n">j</span><span class="p">)[</span><span class="mi">0</span><span class="p">]])</span>
            <span class="k">for</span> <span class="n">j</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">1</span><span class="o">+</span><span class="nb">int</span><span class="p">(</span><span class="nb">max</span><span class="p">(</span><span class="n">label</span><span class="p">)))]</span>

<span class="n">regdat</span> <span class="o">=</span> <span class="p">{</span><span class="n">eachfile</span> <span class="p">:</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="s1">&#39;data/&#39;</span><span class="o">+</span><span class="n">eachfile</span><span class="o">+</span><span class="s1">&#39;regions.csv&#39;</span><span class="p">)</span>
 <span class="k">for</span> <span class="n">eachfile</span> <span class="ow">in</span> <span class="n">files</span><span class="p">[:</span><span class="mi">2</span><span class="p">]}</span>
</pre></div>

<p>With various algorithms and weight functions we can generate many
candidate maps.  In this section we will look at how well they satisfy
the criteria provided by law.  </p>
<p>The AZP regionalization optimizes for keeping racial and ethnic groups
from being divided.  Let's see populations by district to see how well
it does.</p>

<div class="highlight"><pre><span></span><span class="n">regpops</span> <span class="o">=</span> <span class="n">getpop</span><span class="p">(</span><span class="s1">&#39;population&#39;</span><span class="p">)</span>
<span class="n">distpop</span> <span class="o">=</span> <span class="nb">sum</span><span class="p">(</span><span class="n">geodata</span><span class="p">[</span><span class="n">currdat</span><span class="p">]</span><span class="o">.</span><span class="n">population</span><span class="p">)</span> <span class="o">/</span> <span class="mi">7</span> 
<span class="n">spanpops</span> <span class="o">=</span> <span class="n">getpop</span><span class="p">(</span> <span class="s1">&#39;hispanic&#39;</span><span class="p">)</span>
<span class="n">whitepops</span> <span class="o">=</span> <span class="n">getpop</span><span class="p">(</span><span class="s1">&#39;white_nh&#39;</span><span class="p">)</span>
<span class="n">ntvpops</span> <span class="o">=</span> <span class="n">getpop</span><span class="p">(</span><span class="s1">&#39;ntvam_nh&#39;</span><span class="p">)</span>

<span class="n">f</span><span class="p">,</span><span class="n">ax</span> <span class="o">=</span> <span class="p">([],</span> <span class="p">[])</span>
<span class="n">f</span><span class="p">[</span><span class="nb">len</span><span class="p">(</span><span class="n">f</span><span class="p">):],</span> <span class="n">ax</span><span class="p">[</span><span class="nb">len</span><span class="p">(</span><span class="n">ax</span><span class="p">):]</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">(</span><span class="nb">zip</span><span class="p">(</span>  <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>  <span class="p">))</span>
<span class="n">plt</span><span class="o">.</span><span class="n">bar</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="mi">7</span><span class="p">),[</span><span class="n">i</span><span class="o">/</span><span class="p">(</span><span class="n">j</span><span class="o">+</span><span class="mi">1</span><span class="p">)</span> <span class="k">for</span> <span class="p">(</span><span class="n">i</span><span class="p">,</span><span class="n">j</span><span class="p">)</span> <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span><span class="n">spanpops</span><span class="p">,</span> <span class="n">regpops</span><span class="p">)])</span>
<span class="n">ax</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s1">&#39;Hispanic Proportion of each District&#39;</span><span class="p">)</span>
</pre></div>

<div class="highlight"><pre>
Text(0.5, 1.0, &#39;Hispanic Proportion of each District&#39;)
</pre></div>
<img src="data:image/png;base64,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" width="600"/>

<p>District 6 has a high proportion of
people who identify as hispanic, almost a majority.  In this
hypothetical districting map, any candidate would have to address the
concerns of this group.</p>

<div class="highlight"><pre><span></span><span class="n">f</span><span class="p">[</span><span class="nb">len</span><span class="p">(</span><span class="n">f</span><span class="p">):],</span> <span class="n">ax</span><span class="p">[</span><span class="nb">len</span><span class="p">(</span><span class="n">ax</span><span class="p">):]</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">(</span><span class="nb">zip</span><span class="p">(</span>  <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>  <span class="p">))</span>
<span class="n">plt</span><span class="o">.</span><span class="n">bar</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="mi">7</span><span class="p">),[</span><span class="n">i</span><span class="o">/</span><span class="p">(</span><span class="n">j</span><span class="o">+</span><span class="mi">1</span><span class="p">)</span> <span class="k">for</span> <span class="p">(</span><span class="n">i</span><span class="p">,</span><span class="n">j</span><span class="p">)</span> <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span><span class="n">ntvpops</span><span class="p">,</span> <span class="n">regpops</span><span class="p">)])</span>
<span class="n">ax</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s2">&quot;Native American Proportion of each District&quot;</span><span class="p">)</span>
</pre></div>

<div class="highlight"><pre>
Text(0.5, 1.0, &#39;Native American Proportion of each District&#39;)
</pre></div>
<img src="data:image/png;base64,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" width="600"/>

<p>District 6 tends to maximize the
Native American population.  However it is a lower fraction of the
total population, and even in this district only comes to 
' 1%'.<br />
Even though this regionalization does have a region with high Native
population, their voting power is still diluted with other (mostly
white) groups'.</p>

<div class="highlight"><pre><span></span><span class="n">f</span><span class="p">[</span><span class="nb">len</span><span class="p">(</span><span class="n">f</span><span class="p">):],</span> <span class="n">ax</span><span class="p">[</span><span class="nb">len</span><span class="p">(</span><span class="n">ax</span><span class="p">):]</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">(</span><span class="nb">zip</span><span class="p">(</span>  <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>  <span class="p">))</span>
<span class="n">pwhite</span> <span class="o">=</span><span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([</span><span class="n">i</span><span class="o">/</span><span class="p">(</span><span class="n">j</span><span class="o">+</span><span class="mi">1</span><span class="p">)</span> <span class="k">for</span> <span class="p">(</span><span class="n">i</span><span class="p">,</span><span class="n">j</span><span class="p">)</span> <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span><span class="n">whitepops</span><span class="p">,</span> <span class="n">regpops</span><span class="p">)])</span>
<span class="n">plt</span><span class="o">.</span><span class="n">bar</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="mi">7</span><span class="p">),</span><span class="n">pwhite</span><span class="p">)</span>
<span class="n">ax</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s2">&quot;Proportion White in each District&quot;</span><span class="p">)</span>
</pre></div>

<div class="highlight"><pre>
Text(0.5, 1.0, &#39;Proportion White in each District&#39;)
</pre></div>
<img src="data:image/png;base64,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" width="600"/>

<p>For comparison here is the white population in each district.  Only in
District [] are they less than the
majority.</p>
    <HR/>
    <div class="footer">
      <p>Published from <a href="DistAnalysis.pmd">DistAnalysis.pmd</a>
    using <a href="http://mpastell.com/pweave">Pweave</a> 0.30.3
    on 02-11-2019.<p></div>

            </div>
        </div>
    </div>
  </BODY>
</HTML>
