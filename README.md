About
=====
Takes the symbol file produced by <code>jtool -j &lt;kernelcache&gt;</code> and imports any of the symbols that have been discovered by the program.

It does not import symbols labeled as <code>&#95;func&#95;</code>

Usage
=====
Generate the symbol file using:
<pre><code>jtool -j &lt;kernelcache&gt;</code></pre>
with a decrypted kernelcache

Then ensure that that file produced by is in the current working directory where IDA is analysing the kernelcache
<b>Advised to rename the file to kernelcache.sym or something easier to remember</b>

Now load the script into IDA with <code>File->Script File</code> and select <code>ida_load_joker_sym.py</code>

The python utility will be imported as <code>imp</code>

Now run the script using <code>imp.import_symbols("&lt;kernelcache.sym File&gt;")</code>

Reloading the module after change
=================================
If you have altered the python script while the file was already imported into IDA you can simply import it again using <code>File->Script File</code> and select <code>ida_load_joker_sym_reload.py</code>