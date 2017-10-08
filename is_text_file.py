    import string, sys

    text_characters = ����.join(map(chr, range(32, 127)) + list(��\n\r\t\b��))
    _null_trans = string.maketrans(����, ����)

    def istextfile(filename, blocksize = 512):
        return istext(open(filename).read(blocksize))

    def istext(s):
        if ��\0�� in s:
            return 0
       
        if not s:  # Empty files are considered text
            return 1

        # Get the non-text characters (maps a character to itself then
        # use the ��remove�� option to get rid of the text characters.)
        t = s.translate(_null_trans, text_characters)

        # If more than 30% non-text characters, then
        # this is considered a binary file
        if len(t)/len(s) > 0.30:
            return 0
        return 1

		�����㷨�������£�

#���Ƕ������ļ����д���ֻ��ָ��һ���жϵ�־���С��������ĳ�����512���ֽڡ�
#��������Ĵ��а�����\0������ļ�Ϊ�������ļ������������Ϊ�գ�����Ϊ���ı��ļ���
#Ȼ����ͨ��һ�����˴����������ı��ַ����˵������ж�ʣ�µ����ݵĳ�����ԭ�ı��ĳ���֮�ȣ��������30%�����ж�Ϊ�������ļ�������Ϊ�ı��ļ����㷨����ͦ�򵥵ġ�Ҳ����õ��ϡ�

#���Ǵ�cookbook�����ģ�Ӧ�ò��ʺ������ĵ��������Ϊ��ֻ������С��127��ascii�ַ��������Ķ��Ǵ������ġ�ֻ����һ���ο���