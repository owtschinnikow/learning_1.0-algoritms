#coding: utf8
#== сжатие и распаковка по Хаффману ==========================

#== вспомогательные функции =========================== 
#-- элемент для работы:   a = (количество, символ)

#-- сравнение 2х эоементов по количеству ----
def fn_cmp(a,b):
    if a[0] > b[0]: return 1
    if a[0] < b[0]: return -1
    return 0

#-- создать дерево хафмана по тексту ----
def make_tree(text):
    #-- построить отсортированный по список ( частоте, символ )
    se = set(text)
    ls = [(text.count(ch), ch) for ch in se]
    ls.sort()#(fn_cmp)

    #-- построить двоичное дерево по этому списку
    while len(ls) >= 2:
        d = (ls[0][0] + ls[1][0],(ls[0][1], ls[1][1]))
        #print d
        if ls[-1][0]< d[0]:
            ls.append(d)
        else:
            for num in range(2,len(ls)):
                if ls[num][0]>= d[0]:
                    break
            ls.insert(num,d)
        ls.pop(0)
        ls.pop(0)
    return ls[0][1]

#-- рекурсивно создать бинарный код листов элемента ----
def fn_cod(st,el):
    global ls_haf
    if type(el) == str:
        ls_haf.append( (el, st) )
        return
    fn_cod(st+'0', el[0])
    fn_cod(st+'1', el[1])
    return

#-- создать словарь хафмана по тексту ----
def make_dict(text):
    global ls_haf
    ls = make_tree(text)
    ls_haf=[]
    fn_cod('',ls )
    dc_haf= dict(ls_haf)
    return dc_haf

#-- сжать по хаффману
def compress(text, dc_haf):
    st_res = ''
    for ch in text:
        st_res = st_res + dc_haf[ch]
    return st_res

#-- decompress
def decompress(text, dc_haf):
    dc_decod = { dc_haf[key]:key for key in dc_haf}
    st_res = ''
    while len(text) > 0:
        num = 1
        while text[:num] not in dc_decod:
            num+=1
        st_res += dc_decod[text[:num]]
        text = text[num:]
    return st_res

#== Собственно программа ====================================
text = 'preved medved'

#fh = open('hafman0.py')
#text = fh.read()
#fh.close()

dc_haf = make_dict(text)
compressed_text = compress(text, dc_haf)
decompress_text = decompress(compressed_text, dc_haf)

print ('text: ', text)
print ('dc_haf: ', dc_haf)
print ('compressed_text: ', compressed_text)
print ('decompress_text: ', decompress_text)

#fh = open('hafman01.py','w')
#fh.write(decompress_text)
#fh.close()


