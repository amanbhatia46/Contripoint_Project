           X      ���������+��~���Q#���*�X��            (�/�`X � V3 `g� m�$�+�r6v�7La�3�kcC���,�) ( ( ?��k�x���l��\���`h�&ɶ�:q����� �Qő��+���kd|�O�W
~
��b�e\RgdO���z�%�j3nQ�7�ˏT2A��ݜ���x���욊�מ����\o%����d�>~B�Cx�dje�E�k�A0P8<�7�jyh�h P��LGc�ER�fg���2���"Ȱ��v,          -  R      �    �����N"�@�I�\f����E"               �      !envlist = py26, py27, py33, py32
    -    A  X     �   ����>~��+ckb�b��߮@            (�/�`|�	 �3*���   �%2ٶJ4y�>eY�gi����^�r�;��g��T�kƇ�u�<�)[!���D^SAe���*�߉��f�jXF���(+��d��MNֽ)-��B��ZJ�M��Yl�\��6w�ĖÞ��{ʞk�|����jV��5eO��Dl����Y����LBUՀCu9�s�/���Q,�������M��
p�N�j, `�1z���6t�AK
va���4����$�x��y��ᕍ;l:�7!���L��"��$������!ސB�Aj��q&��	5�� C�	��0���ı�    n     �  �     �   ����b�@g�w(�Z�g��o&�%            (�/� �e ��!�� ���WI�H���A���zw�z���%�}�*1��c w�N����"�;����n�d�а�V�H��*1��vUc���-��$�3@�v��6�DD �" g�8؂�F.��?/��׀�c�1         Q  �     T   �����0)��	T���r	�6S/&�4               �  9   Eenvlist = py26, py27, py33, py32, nolxml, lxml, nopillow, xfail, doc
    T     '  L     ]   �����k(w-�a�TXR��,;
Io4�               �     envlist = py26, py27, py33
    {        �     _      �hl���x�J���! /t����                {        �     c      1���*�^$�(�i�Я	q�                {     0  �     x   �����v������t��!���*W�              z  �      �  �      E  N      �  �        �     P  �     ~   ������kLU�.���%�y}���              �  �   ,    lxml
setenv =
    OPENPYXL_LXML = False
  �  �       py.test
    �     a     	     	�����o���;�󓼊>���v��            (�/� g� E��	̳��ob����6%��[��07S�dȹ��Rޜ=��9��s���Z����?��fs!U�es��C! ,B5/p��    \     �  �   
  �   
������P����r������E�            (�/�`6 U �	$*��	ϳ�mē���"�ޔ��v�a�Z�b��	l�1fp32˖z��o˿-���e���KR�>C%�MIq�X��t��j�a���Tm6}�}�ؕvu,��������$YEBh��2(��8���&3�B\��ؔ��� !#�>eĽa;�Ҷ2pi�@�h�5��]f��g�!I��i �r]���� �L%    0     M  �     �   ����Zw>�i�E%��+���m<�=            (�/� t% �    b   h    py26,
7323nolxml-pillowxfail,
 L哃W�}��a�1    }     w  7     �   ����ꥃ�?Dו�gg�g�            (�/� �u ��'�� L"B��)�L�8I"ˮ�-BOr���֋F(K^I�޼�3��əIQS���%�f%���-9�16h�xP�-�%��i� t5��25�w��{pD    �       @     �   ������R�`���C~�P��|�$Ա              �  �   	    lxml
    	     �  _     �   ������G<?��7I1͑��Go�~            (�/� �� �	$)��<  P�s:����o�}�΀&�Y�C����26���ίD8�VUOR�n�u�YD��#5,�Ϯ���?����:�Ieq/�#do�,���HB�JoZ�T��	�n
����e�X�D�ξSm9vd&b�Y�� 9���iD0p��@�v���`��h��w�8ƎU�    �        _     �      X��V��K6 �q���x�                �        @     �      �ܯ}G@k���R8�@��y                �       J        ������,���^���et`�F�,              +  +   
    py34,
    �     X  e        ����$��4����8������Y��            (�/� d} �   �  K   Xenvlist = py26,73324, nolxml-pillow, xfail, doc
 6	@5�
����<    7     �  T     &   ���������W{��NK,��qn            (�/�`, �   R !    keep_vba,
-py33,
   �[testenv:]
deps =pylxml
seOPENPYXL_KEEP_VBA = True
command.
]
basepython =hon3.3 ��)�0�Xo�KB0 aPi�2si ��\	^����׃#    �       ^     '      �1e�
O�V��+� ��e̍�              +  +   
    py34,
    �        ^     _      ����{s<K�^6��V]N0��                �     5  o     �   ����-{���p�#�JE'p���0�              \  {   )commands = {envbindir}/py.test {posargs}
    '     5  h     �      nY0Z,��ڲ(/l��a&�Xy              �  �   )commands = {envbindir}/py.test {posargs}
    \     7  a     �   ����^z��v0Z�vo���ˈ�ՏZ              �     +    py.test openpyxl/tests/test_backend.py
    �        h     �      �ڬcʈ�ܱv���a����@                �     S  �        ������!�w��!���˹����            (�/� YU �  � M    sphinx-build -W -b doctest -d {envtmpdir}/rees .est
 `
�dp�    �       �     h   ����h�49i!'֭�?�A1	|              +  5   
#   py34,
    �       �     }   �������G��|[{�� ��4���              +  5   
    py34,
    	       �     �   ������[�e�|�6������bs                !        	     a  �     �   �����H�KV�\GUjWG��EQ1v��            (�/� �� �D�5 �?ڱ�}��B������v�A���y;=m^�wc�����ք[�z�Z��sek@�pKA�$3��)�� �P3u�#�9��cB    	       �     �      o]�gJ��a�T�C��i|                !        	�     V  �      	;    ����uKͿ���eU�Y�V�:D��            (�/� Wm 2��W�3���%���0��L�~��@?�l!�U�	�P�l<��#��H��ᶉ��9�O��? �
k3/�Yr�z    	�     l     !  	�   !�������̧��/u0��-��Z2�            (�/� v ���9σ��͂v"H�?W�>V0�`K>F�KȲ(�")	��o�d��� T
����l$��U�	] Z+q�0u�h�8-� A�P��ʬ0    
M     �  
i   "  
   "����0ߡ��a�����b��L�            (�/�`r] R�$p�m �L�Wd�J�~���Hp��h���k�n~�C���M�|Q����hR�ѕRԇ�"W�7.ҿ��*r�4.H�>k�hUlV��"~J��|a��I��)ut�Y���]������<�r��0�i�pJ� qqH�C�D���]  @   ��,s�b���2p� �?�Đe�4@��,$r�7H��q��q�� /7���:^g>Y���u�s�E���     B     x  
�   #  
   #����L�oUº+�ܴl��C1�            (�/� �} bF ��	0Z�˭��E�O��\tg8� "N0����4A�6�b9�J���t�����px#i��1m�&����-��l�W�OA?�>8�b�LB��:�� Y�4eϘ�    �     J  
�   $  
   $����y�GX�-�(1b��{�WQ�d&            (�/� � T    �       py.test {posargs}
  �  �s  �  	 ���.*�*         -  
�   %  
V   %�����́tb7�	���d�!�{"!9              `     !    sphinx-apidoc -f -T -o api \
    1       
�   &  
b   &������v��	�� �����<��              }  }       pillow
    H       
�   '  
�   '�������?�Ad�q�Xi<              r  r   	    lxml
    ]     ^  h   (  
�   (����h���		\>���� o}            (�/� �� d  � w    {toxinidir}/openpyxl/workbook/external/conftest.py \
_.py \
 J �* W�9"    �     <  !   )  
�   )����L)�,/�4�B��f���2�<�              �  A   0    {toxinidir}/openpyxl/workbook/names/tests \
    �       
�   *  �   *����9L�4���]�4UL��_y�[G              :  p        O             T  
�   +  �   +����8�8?F"	Mw0��2@.����            (�/� d] �  � %    {toxinidir}/openpyxl/classify/ \
  . 'utils/tests \
 T-<0ʃ�    c     9  
�   ,  �   ,����q(���7������V�
A7              _  �   -    {toxinidir}/openpyxl/descriptors/tests \
    �     8  
�   -  �   -����� �6��^��'q[%�����              �  �   ,    {toxinidir}/openpyxl/worksheet/pivot.py
    �     <  
�   .  a   .����V��Ze)"���n)5@��Y              �  �      �  �   $    {toxinidir}/openpyxl/develop/ \
         \     /  �   /������!BRG�K�;6ۆlP�.            (�/� l� �  �  �   `    {toxinidir}/openpyxl/worksheet/pivot.py \
riter/dump_.py
 ]^���    l     5     0     0������:�D$��E�]���x�            (�/� 8e D    $   changedir = doc
  }  � |z>    �     3     1     1�����Dw�0(qZ��6�5&9	jY�              Y  z   '    sphinx-apidoc -f -T -e -M -o api \
    �     7  =   2  '   2����L}Y�*���`�m�R�*                   +    {toxinidir}/openpyxl/packaging/tests \
           
�   .  Y   .�����7�qRP��"�<��@�ʽ�              �  �   passenv = LANG
    &       L   3  Z   3   49"�7d-l�+
-Ya�(��              �  �   passenv = LANG
    A     U  J   5  �   5����4'�o��lG��r�AKNhv|              	�  
!   I    py.test openpyxl/drawing/tests/test_image.py::TestImage::test_import
    �     3  I   6  �   6�����\�P�7ǀ�[��{�              �  �   '    {toxinidir}/openpyxl/chart/tests \
    �     9  v   7  �   7�����ݬx\�c�N*���zW�              �  �   -    {toxinidir}/openpyxl/utils/formulas.py \
         0  �   8  |   8����%v��~�]l]meXd� �l              �  �   $    {toxinidir}/openpyxl/formula/ \
    2     i  �   9  .   9����k�0�&��đ܎7��F>P            (�/� l   �  �   +    py.test openpyxl/s_backend.py
  
�  
�   )commands =-rx -m xfail
 N�� ԧ�MX�	    �     i  �   :  5   :�����`aH
f�k�m&�H���            (�/� p �  + 
    py35,
  `  s   keep_vba-py34�  	   /[testenv:]
basepython = 3.4
 ,C}��B�'g.         o  +   ;  v   ;����f���҆���]ϙ�ʵ*Ca            (�/� {5 �F�����/CJ�$߿M*�=Vc\d*\f@s��	�t��t�X�p���ތX�r&P!S��<���Rs��k���y�0�R#P��fJ B 2璤�ypY    s     G  [   <  �   <����Y� ��P���;�2D��#D              �     ;    git+https://github.com/nicoddemus/pytest@param-ids-fix
    �       +   =  �   =�����J8ٌ�ؒ�Nn�����              �  2       pytest
    �       3   >  �   >������Ż{���/�q�1x�i              �         pytest < 2.8.1
    �     D  ;   ?  �   ?�������˵�<�QH>�����<              0  `   8    {toxinidir}/openpyxl/workbook/external_link/tests \
    4       +   ?  �   ?�����a��l�F���F�7.nE�              �  
       pytest
    K       3   @  �   @   A�j���d�Ì��/㍈?J              �  
       pytest
    b     7  O   B  �   B�����s�K�������L���	              �  �   +passenv = LANG PIP_FIND_LINKS PIP_NO_INDEX
    �       V   C  �   C����IUl��,�ʙv�A�%ԑǿƃ                '       lxml==3.5.0
    �     E  �   D     D����޺���b1@���y�
�>                        !      A  R        .   	    lxml
  	�  
1        �     w  �   D  >   D������m��d����TO7b�s�            (�/� �u ���3 ��~�$��x$v٘�������k�r�c�E��
��
��	m�|a:�J�F�Ps�>)���AO ��`Lg�?p�.	 iHl=¾KP�M%$Pc�>�,    q     E     F  ?   E   FB��->�j6�hs��9��                        !      A  R      *  :   	    lxml
  	�  
=        �     o  (   F  B   F����L�=��sE|�$p���8^��            (�/� z5 B��)��4��"]�dazt�QZ�k�ew�X�jnrL�P�
������c�3*J)9�ڤhs���?伉G`����l��aL`��,  j]����    %       '   H  L   H����R�(���p��w8L��\��<              �  �   [testenv:numpy]
    A     *  9   I  P   I������jU�\��W�6s��X�Ki              E  E   	    lxml
  �  �   	    lxml
    k     E     J  Q   G   J�5`A��;����0��{#G�                        !      A  R      *  :   	    lxml
  	�  
=        �          J  �   J����Pf�!��8�D�ϖ(��              
  0        �       Y   K  �   K   L=��Z8��uZz==-c!]��              �          �     P  K   L     L�����n�(iR"�@����=��M��^              �  �       pandas

  0  0   ,    {toxinidir}/openpyxl/chartsheet/tests \
         E  �   N     M   N���>����EqR���M�	y��                        !      A  R      *  :   	    lxml
  	�  
O        ]     8  W   A     A����s+���w	s�ی��fP)              �  �   ,    {toxinidir}/openpyxl/chartsheet/tests \
    �     >  K   N     N   P��ބ�*Ln6�9���м�5d�              �  �   &    {toxinidir}/openpyxl/cell/tests \
    <        �     E  �   Q     O   QU�7��ΠH#������y���                        !      A  R      *  :   	    lxml
  	�  
O               U   Q  �   Q�����\�>��fc��x��3_ı�              5  5   
    py36,
    .       �   R  �   R   S��x�|sy e�n��Pkk
��              !  !   
    py36,
    D       [   S     S����Z�C�����'�]���              D  O       pillow<3.5.0
    a        �   T     T   Ur���&�m- Yy]	��dz                a     #  r   U     U����<0?��!�t��(.Nku�AR              i  i   basepython = python2.7
    �     #  �   T     V   W!�&[��qmRט0�r)`�L              7  7   basepython = python2.7
    �     �  �   W  '   W����.3V���O2� ��]����            (�/�` U 2K'+��$ *IRq4]�d�U��e��2�N$I��]cd0A���߾Z$��0B�q�����P�	�zM3�/���0u��=2z����ikOd�gP�|�޳�5� ���0q��hc�c�T��"}��(�"��@I׭}r:O�	�-��_p|��T�t33�+ GH4��s+� '�7Ӓ*Kǆ�b�� �!p��Ά�\    {     P  �   Y  (   X   Y�n[����l搒��¬o�                        !      K  \      4  U       lxml
    pillow
  	�  
�        �     m  �   Y  )   Y����s��0�u���X�+�#�]���6            (�/� �% rE�� ���Wu٢[z���!��sˊ�K�qV�e5��ۍ�g��53Yt�`�(D�"Z*��m�1��R�cM%D�`�p6�� ��b���^�	    8     P  �   [  *   Z   [y��K%�Gk��#�}�Up���                        !      K  \      4  U       lxml
    pillow
  	�  
�        �     �     [  A   [�������MjNt��7��ŏ��            (�/�`  �(�Q$ �0Ke��=��6����"�|��dW#��L�\kǧ��S����q����+FV+�X��r����{���v�������=Ğ�6�W6h�f�X/X�[���x2��Xŝ�&
J	)R'�� O�C�k,���ᖰ4΀f�p43�(g.    3     P  g   ]  N   \   ]����dH*8�y�W��              $  .      8  B      l  }      U  v       lxml
    pillow
  	�  
&        �     M  �   ^  �   ^�����~����8���;M�Z��            (�/� [% �  �  �   O    {toxinidir}/openpyxl/pivot/tests \drawing
 KFҢ�    �     M  �   _  �   _����/��}Vy&py������I���            (�/� \% �  �     P    {toxinidir}/openpyxl/pivot/tests \
drawing LfԢ�        F  �   a  �   ]������N�k�?�$�mM�\,p�            (�/�`�� ��y' ���ZF6{s>�#�Q˱�x���VB����{f���K f k u ���Z鲟�.���}\�����Э���֯�qU��X��Y�]��θ������3tV�}-��Zq���~)ow�.���R�u�����-Z����xDf�U�b����r�w�E�s}n�|�.�eH{Jw�&�Ɓ�� ����l��6h�7��[���>��tR�����Q���a�b��dT։i��Q���s����Z�{gO��e�yΚ�a�@,��Sn��3�:�7c}��X��l�}�-��0�j>�0�0�,,��Zڏ)w�ԢI���s�@ �'���u/��f�A�yc.g��.F95�Ce"MT("*��P�<H��e!*�����D�b�@�n6��.9=^C]�&g�㩤S�j�̨��Y�`&���Ǵ�S)nDQt��Ɩ"�I}�D"�|�r�)�G�S`�@*$�D�C���R$,(���R�X&�������-)4� H0Bb�d�@#E���F`�#�"1A@ i��#&NyB��a�7�A6�x3q���?��9jDU�ymy��Y�Y��A��Z�5��Z�V�����'2'"N��0�;�g	L"���uy.�hh	�L�H�8���8��T(g�����5)��q�o{�-$�r�mH^�����9ɀ�2j�ǇOЃ^��7qER{�"P,a�Tm�gv�"s`���i�$[Ji�k$ �=�����dJ��r�
����Ʈ�)�^�v����uH��U�#avD���D�0E��dd�>4��@,c�R�5�udVm=�k��LVm�6�    c     P     a  �   `   a}���|C����YuZj���z�              $  .      8  B      l  }      U  v       lxml
    pillow
  `  �        �          b  i   b�����}L�#�#W�"�Z���{              �  �   
    numpy
    �       '   c     c����u��5X�;�r�G!���N�s��              L  L   
    py37,
    �     d  �   d     d����L:�f!�jAm��] *���            (�/� ��   V     pypy,
3,
  Z e[testenv:]
se =OPENPYXL_LXML = False


3	 T-�j�\uC�k0-'e�n��    C    <  �   e     e�������$�}�֖�`ç�K            (�/�`H�	 �<1�9I l�X�R6��,n"3�$3I$�䋜�t���n������-�w�. 0 . ;��Zk?����:բ�^�Ӱ�X6�����\N��Z��E��h|����0z�'��ՕLS6!k�-	%� ~�� eRɵP�2��e�Mky��s��ٌ��K����0�Y:���o���c<_q���iѵu�%a�0�H�,u�E9�0�������+n����AɥH���π>� l+�� �D�H#\�h�ƻ�I#(��܂� ���(�@Ղ�����.�m,F���Qf         �  �   f     f����Zo\�9�������aQ            (�/� � �pi�$�짻�j�;�T��جϪf�������.H��J�d�G4#O� ɬ��Y��5���؛%��qʐd����#�.ҮzJ��C38�9DK^AIS��١���l � � ��̓�          1  �   g  %   g����n������?�m�If���3V              /  S   %passenv = COVERALLS_REPO_TOKEN GIT_*
     9     �  �   f  3   f����L���́�ͬ74�KO���            (�/� � "H!`A+ ���_���&�Eo��6�a}�T�V�>���.H��J�d��hF��A�Y�ϳ^�k4�_��#.JF��,�!����݀��H�J�ቆp�s������p��C����A� � 9��̓�     �        �   h  4   h   i���z9�#˘�����o                 �     �  �   h  �   j����<�V|z��砾,X�5=1
���            (�/� �� �$�)�$  E3iXM���:��\���y~J"TX��{�<'����a�|��qڨ(���	��|�ӃJF��NP8�\���i*H�"jw���_��> ��+��#%h\wCܺ�    !J     �  a   k  �   k�����84ܕ=Q���{�8�%t            (�/� �� ��#�k o��x[�)��)�r՝�x.�'a�6�İ���� ~I~��g��=��:�(�M�6%���_�|�.J�Z�����!"��sMA�\��{�'�� b  �J-a�:cpm�T,�O    !�     "  w   l     l�����C��c6�AJ��墋i�[.a              �  �       pillow
    pandas
    !�     L  @   m     m�����`y�
_Z��?�տ�M]�            (�/� \ d  $  B V  ` k  �   8    {py37}-nolxml,
keep_vba
 4'�ft@��    "<     -  �   i  -   i����xc�_����m�)�V)��Կ��              �     !passenv = LANG PIP_PREFER_BINARY
    "i     -  m   m  /   m   o��)>,�D\�^P�j�u��                .   !passenv = LANG PIP_PREFER_BINARY
    "�       c   p  0   p����W�/K�3�:�嵐$�eL              .  8        "�     -  6   n  1   n   qsȞl������O�V�
j@k              �  �   !passenv = LANG PIP_PREFER_BINARY
    "�     A  �   o  3   o�����yǃ7��^��������%�,              �     5passenv = LANG
setent =
    PIP_PREFER_BINARY = True
    #     A  w   q  4   q   s��,�jU��������h�              �     5passenv = LANG
setent =
    PIP_PREFER_BINARY = True
    #Q     L  J   t  6   r   t���TY�Xy�u�Q�aR��T>            (�/� \ d  $  8 L  V a  �   8    {py37}-nolxml,
keep_vba
 4'�ft@��    #�     o  	�   i  �   i����oSa�!���aZ���7-0*            (�/� �5 �  � �
[testenv:defusedlxml]
deps =
    {]}xml
noseOPENPYXL_LXML = False


	 r$ ��3"�D�����r8kQ�<�,    $     A  	�   v  �   s   v��V�+o�:�y����*�>              �     5passenv = LANG
setent =
    PIP_PREFER_BINARY = True
    $M     r  	   t  �   t   w/_V����%��?���]�[            (�/� �M �  � �[testenv:defusedlxml]
deps =
    {]}xml

:noseOPENPYXL_LXML = False



 r$ ��3BD��	E�����p.���sD    $�     �  	h   x  �   u   x�I6�
[�r^{@�3b���            (�/� � ����	�u@ 5:+)e4�3�CvF-{�� �_�|�[в+�{��Y:����y�ȦVbf��1�1i�*���)l!f٭�&qTef2�_�O��
<� �*�CV�fh�S0��͍�i�n�    %H     g  
   w  �   w����qI}B ��V�8�`PD���,            (�/� �� �  � $    defusedlxml,
no  3 )commands =pytest -xrf openpyxl/xml

  � ( �*���Z�abs�4MxpY    %�     f  	�   x  �   x   z�CS�	FMZ�"jo�s�C            (�/� �� T  � $    defusedlxml,
no  # )commands =pytest -xrf openpyxl/xml
� ( �*�CV��jt��́�4��e    &        	h   y  �   y   {j1��Ei������@�UXA�                &       	r   y      |�����rfkҮ�]�j��xg��              8  8   
    py38,
    &+       	�   {   �   {�����%3���R_�aR�E��{�              �  �       pillow < 4.0.0
    &J     ,  	�   ~   �   ~����Wf��ͨ=�	�q���y��b�              ,  5   	setenv =
  �  �       pillow
    &v       	r   }   �   }   �\�l�ٌ��HB܍�����              
     	setenv =
    &�     =  �   �  !)   ������Ȇ�q���}E�HnObFƥ              M  q       defusedxml,
  �  g   [testenv:defusedxml]
    &�       �   �  !R   �����:�������C�ֿ�����8(              B  B   
    py39,
    &�       		   �  !l   �����,u���3����z���v.hN              �  �   depends = doc
    &�     ;  	   �  "   ��������K�<{D��u���Z�ve              t  t       pandas: pandas
  �  �   [testenv:pypy3]
    '3     ,  �   �  "�   ������t!�^�@�������+              �  �      �  �   basepython = pypy37
    '_     L  	   �  "�   ������ٔ|���s�
�J�?b�n^�*              �  �   4[testenv:pypy]
setenv =
    OPENPYXL_LXML = False


  �  �        '�     V  	   �  "�   ������W+"h��)6��j1��t���            (�/� hm �  $  8 L     py310,
  g  �   9{py38}-nolxml,
keep_vba,
 4'`3j:�ak�    (     G  	7   �  "�   ������"�&SX���
N�����5              �  �   ;setenv =
    basepython = pypy38
    OPENPYXL_LXML = False
    (H     G  	7   �  "�   ������u���~���|F6�vy              �  �   ;setenv =
    basepython = pypy37
    OPENPYXL_LXML = False
    (�        	7   �  "�   �   �A�T)S�����o�Ձ�ݪr                (�     V  	.   �  "�   �   �S��[�!N��K�bWG٪n            (�/� hm �  $  8 L     py310,
  g  �   9{py38}-nolxml,
keep_vba,
 4'`3j:�ak�    (�     $  	.   �  "�   �����q@�h,S���J�8��              �  �       basepython = pypy37
    )	     +  	   �  #R   ������ ��
��|'0���	?����              �     setenv = OPENPYXL_LXML = False
    )4        	   �  #S   �   �#
���N�|~:�Ҏ���                )4     G  	.   �  #T   �����J�^2�Sߵ���츞�p@*              �  �   ;setenv =
    basepython = pypy37
    OPENPYXL_LXML = False
    ){     "  	M   �  #�   �����$"u3A����������+8�              L  L       py310,
    py311,
    )�     O  	^   �  $   �������ݧ�z����I�R��t
_�            (�/� U5 ���
�#��D���p+\�&��|�I8e���
��B��kzP	���)�w�6���0�`� zJ�f    )�     E  	J   �  $   �   � 4tO��4C���k�Ȍ|��?            (�/� Q�   $  8 }  �   9    {py38}-nolxml,
keep_vba,
 4'�ft8