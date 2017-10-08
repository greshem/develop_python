    import string, sys

    text_characters = “”.join(map(chr, range(32, 127)) + list(“\n\r\t\b”))
    _null_trans = string.maketrans(“”, “”)

    def istextfile(filename, blocksize = 512):
        return istext(open(filename).read(blocksize))

    def istext(s):
        if “\0″ in s:
            return 0
       
        if not s:  # Empty files are considered text
            return 1

        # Get the non-text characters (maps a character to itself then
        # use the ‘remove’ option to get rid of the text characters.)
        t = s.translate(_null_trans, text_characters)

        # If more than 30% non-text characters, then
        # this is considered a binary file
        if len(t)/len(s) > 0.30:
            return 0
        return 1

		整个算法大致如下：

#不是对整个文件进行处理，只是指定一个判断的志块大小，象上面的程序是512个字节。
#如果读出的串中包含”\0″则此文件为二进制文件。如果读出串为空，则认为是文本文件。
#然后先通过一个过滤处理，将所有文本字符过滤掉，再判断剩下的内容的长度与原文本的长度之比，如果大于30%，则判断为二进制文件。否则为文本文件。算法还是挺简单的。也许会用得上。

#这是从cookbook看到的，应该不适合有中文的情况。因为它只考虑了小于127的ascii字符，而中文都是大于它的。只能做一个参考。