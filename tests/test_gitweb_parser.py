import unittest

from gitweb import GitwebHTMLParser


class TestGitwebParser(unittest.TestCase):
    sample = """<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en-US" lang="en-US">
<!-- git web interface version 2.20.1, (C) 2005-2006, Kay Sievers <kay.sievers@vrfy.org>, Christian Gierke -->
<!-- git core binaries version 2.20.1 -->
<head>
<meta http-equiv="content-type" content="application/xhtml+xml; charset=utf-8"/>
<meta name="generator" content="gitweb/2.20.1 git/2.20.1"/>
<meta name="robots" content="index, nofollow"/>
<title>localhost Git - .git/tree - dir1/</title>
<link rel="stylesheet" type="text/css" href="static/gitweb.css"/>
<link rel="alternate" title=".git - history of dir1/ - RSS feed" href="/?p=.git;a=rss;f=dir1" type="application/rss+xml" />
<link rel="alternate" title=".git - history of dir1/ - RSS feed (no merges)" href="/?p=.git;a=rss;f=dir1;opt=--no-merges" type="application/rss+xml" />
<link rel="alternate" title=".git - history of dir1/ - Atom feed" href="/?p=.git;a=atom;f=dir1" type="application/atom+xml" />
<link rel="alternate" title=".git - history of dir1/ - Atom feed (no merges)" href="/?p=.git;a=atom;f=dir1;opt=--no-merges" type="application/atom+xml" />
<link rel="shortcut icon" href="static/git-favicon.png" type="image/png" />
</head>
<body>
<div class="page_header">
<a href="http://git-scm.com/" title="git homepage"><img alt="git" class="logo" height="27" src="static/git-logo.png" width="72" /></a><a href="/">projects</a> / <a href="/?p=.git;a=summary">.git</a> / tree
</div>
<form method="get" action="/" enctype="multipart/form-data"><div class="search">
<input name="p" type="hidden" value=".git" />
<input name="a" type="hidden" value="search" />
<input name="h" type="hidden" value="HEAD" />
<select name="st" >
<option selected="selected" value="commit">commit</option>
<option value="grep">grep</option>
<option value="author">author</option>
<option value="committer">committer</option>
<option value="pickaxe">pickaxe</option>
</select> <a href="/?p=.git;a=search_help" title="search help">?</a> search:
<input type="text" name="s"  />
<span title="Extended regular expression"><label><input type="checkbox" name="sr" value="1" />re</label></span></div>
</form>
<div class="page_nav">
<a href="/?p=.git;a=summary">summary</a> | <a href="/?p=.git;a=shortlog;h=HEAD">shortlog</a> | <a href="/?p=.git;a=log;h=HEAD">log</a> | <a href="/?p=.git;a=commit;h=HEAD">commit</a> | <a href="/?p=.git;a=commitdiff;h=HEAD">commitdiff</a> | tree<br/>
<a href="/?p=.git;a=history;f=dir1;h=68934ea9cf45b01893b50a17fbdf92c482eda892;hb=HEAD">history</a> | <a href="/?p=.git;a=tree;f=dir1;hb=HEAD">HEAD</a> | <a href="/?p=.git;a=snapshot;h=68934ea9cf45b01893b50a17fbdf92c482eda892;sf=tgz" title="in format: tar.gz">snapshot</a><br/>
</div>
<div class="header">
<a class="title" href="/?p=.git;a=commit;h=HEAD">add sample</a>
</div>
<div class="page_path"><a href="/?p=.git;a=tree;hb=HEAD" title="tree root">[.git]</a> / <a href="/?p=.git;a=tree;f=dir1;hb=HEAD" title="dir1">dir1</a> / <br/></div>
<div class="page_body">
<table class="tree">
<tr class="dark">
<td class="mode">drwxr-xr-x</td>
<td class="size">&nbsp;</td>
<td class="list"><a href="/?p=.git;a=tree;hb=HEAD">..</a></td>
<td class="link"></td>
</tr>
<tr class="light">
<td class="mode">drwxr-xr-x</td>
<td class="size">-</td>
<td class="list"><a href="/?p=.git;a=tree;f=dir1/dir2;h=750f28070777c369e0945ac0dc92cee03dde6f23;hb=HEAD">dir2</a></td>
<td class="link"><a href="/?p=.git;a=tree;f=dir1/dir2;h=750f28070777c369e0945ac0dc92cee03dde6f23;hb=HEAD">tree</a> | <a href="/?p=.git;a=history;f=dir1/dir2;hb=HEAD">history</a></td>
</tr>
<tr class="dark">
<td class="mode">-rw-r--r--</td>
<td class="size">0</td>
<td class="list"><a class="list" href="/?p=.git;a=blob;f=dir1/f1;h=e69de29bb2d1d6434b8b29ae775ad8c2e48c5391;hb=HEAD">f1</a></td>
<td class="link"><a href="/?p=.git;a=blob;f=dir1/f1;h=e69de29bb2d1d6434b8b29ae775ad8c2e48c5391;hb=HEAD">blob</a> | <a href="/?p=.git;a=history;f=dir1/f1;h=e69de29bb2d1d6434b8b29ae775ad8c2e48c5391;hb=HEAD">history</a> | <a href="/?p=.git;a=blob_plain;f=dir1/f1;hb=HEAD">raw</a></td>
</tr>
<tr class="light">
<td class="mode">-rw-r--r--</td>
<td class="size">0</td>
<td class="list"><a class="list" href="/?p=.git;a=blob;f=dir1/f2;h=e69de29bb2d1d6434b8b29ae775ad8c2e48c5391;hb=HEAD">f2</a></td>
<td class="link"><a href="/?p=.git;a=blob;f=dir1/f2;h=e69de29bb2d1d6434b8b29ae775ad8c2e48c5391;hb=HEAD">blob</a> | <a href="/?p=.git;a=history;f=dir1/f2;h=e69de29bb2d1d6434b8b29ae775ad8c2e48c5391;hb=HEAD">history</a> | <a href="/?p=.git;a=blob_plain;f=dir1/f2;hb=HEAD">raw</a></td>
</tr>
</table>
</div><div class="page_footer">
<div class="page_footer_text">Unnamed repository; edit this file &#39;description&#39; to name the repository.</div>
<a class="rss_logo" href="/?p=.git;a=rss;f=dir1" title="history of dir1/ RSS feed">RSS</a>
<a class="rss_logo" href="/?p=.git;a=atom;f=dir1" title="history of dir1/ Atom feed">Atom</a>
</div>
<script type="text/javascript" src="static/gitweb.js"></script>
<script type="text/javascript">
window.onload = function () {
	var tz_cookie = { name: 'gitweb_tz', expires: 14, path: '/' };
	onloadTZSetup('local', tz_cookie, 'datetime');
};
</script>
</body>
</html>"""

    def test_sample_page(self):
        p = GitwebHTMLParser()
        p.feed(self.sample)
        self.assertIn('f1', p.files)
        self.assertIn('f2', p.files)
        self.assertIn('dir2', p.dirs)



if __name__ == '__main__':
    unittest.main()