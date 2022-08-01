#!/usr/bin/env python
# coding: utf-8

# # 파이썬 기초 배워보기
# 
# 이번 장에서는 변수와 상수, 데이터의 타입, 제어문, 함수 등 기본적인 파이썬 문법에 대해 살펴보도록 하겠다.
# 
# ## 상수와 변수
# 
# 프로그래밍의 가장 기본은 **상수**와 **변수**이다. 먼저 아래의 코드를 실행해보자.

# In[1]:


var = 10
print(var)


# 10 이라는 숫자 혹은 문자와 같은 값 자체를 상수(constant)라고 한다. 반면 이러한 상수가 저장된 공간인 var는 변수(variable)라고 한다. `var = 10`은 var라는 변수에 10을 할당(저장)하라는 의미다. `print()`는 결과물을 출력하는 함수로써, var의 내용을 출력한다.

# In[2]:


var = 'Hello World'
print(var)


# var라는 변수에 새롭게 'Hellow World'라는 상수(문자)를 입력하였더니 그 값이 바뀌었다. 

# In[3]:


var1 = 1
var2 = 2

print(var1 + var2)


# var1이라는 변수에는 1이라는 숫자가, var2이라는 변수에는 2라는 숫자를 입력하였다. `var1 + var2`는 1+2와 같으므로 3이라는 결과가 출력된다.

# In[4]:


var1 = 3
print(var1 + var2)


# var1이라는 변수에 다시 3이라는 숫자를 입력하면 `var1 + var2`는 3+2가 되므로 5라는 결과가 출력된다. 이처럼 변수에는 계속해서 다른 상수를 입력할 수 있다.
# 
# ## 데이터 타입
# 
# 파이썬에는 다양한 데이터 타입이 존재하며, 이에 대해 하나씩 알아보도록 하자.
# 
# ### 숫자형
# 
# 숫자형(Number)은 정수나 실수와 같이 숫자 형태로 이루어진 데이터 타입이다. (8진수나 16진수도 있으나 거의 사용하지 않는다).
# 
# 먼저 정수형(Integer)이란 -2, -1, 0, 1, 2처럼 소수점을 사용하지 않고 숫자를 표현한 것이다. 

# In[5]:


type(1)


# `type()` 함수는 데이터 타입을 확인해주는 역할을 한다. 1이라는 숫자의 타입을 확인해보면 int, 즉 정수임을 알 수 있다. 한편 실수형(Floating-point)이란 소수점이 포함된 숫자다. 

# In[6]:


type(1.0)


# 1.0이라는 숫자의 타입을 확인해보면 float, 즉 실수임을 알 수 있다. 일반적으로 1과 1.0은 동일한 숫자라고 생각할 수 있지만, 프로그래밍에서 정수형과 실수형은 엄밀하게는 다른 타입이다. 
# 
# #### 숫자형 연산하기
# 
# 숫자형은 다양한 연산이 가능하다.

# In[7]:


print(2 + 1)


# In[8]:


print(2 - 1)


# In[9]:


print(2 * 3)


# In[10]:


print(6 / 2)


# 파이썬에서는 기본적인 사칙연산(+, -, *, /)을 쉽게 할 수 있다. 이 외에도 다양한 연산자가 존재한다.

# In[11]:


3 ** 2


# 연산자 `**` 는 제곱을 의미한다. 즉 `3**2`는 $3^2$ 을 의미한다.

# In[12]:


7 // 3


# 연산자 `//`는 나눗셈의 몫을 반환한다. 7을 3으로 나누면 몫은 2가 된다.

# In[13]:


7 % 3


# 연산자 `%`는 나눗셈의 나머지를 반환한다. 7을 3으로 나누면 몫은 2가 되며 나머지는 1이 된다.
# 
# ### 문자열
# 
# 문자열(String)이란 문자, 단어 등으로 구성된 문자들의 집합을 의미한다. 파이썬에서 문자열을 만드는 방법은 총 4가지가 있다.

# In[ ]:


"Hello World"


# 먼저 큰 따옴표(")로 양쪽을 둘러싸서 문자열을 만들 수 있다.

# In[ ]:


'Hello World'


# 따옴표(')로 양쪽을 둘러싸서도 문자열을 만들 수 있다.

# In[ ]:


"""퀀트 투자 포트폴리오 만들기"""
'''퀀트 투자 포트폴리오 만들기'''


# 큰 따옴표 3개를 연속(""")으로 양쪽을 둘러싸거나, 작은 따옴표 3개를 연속(''')으로 써서 양쪽을 둘러싸서도 문자열을 만들 수 있다. 따옴표를 3개 사용할 경우 줄 바꿈을 통해 여러줄의 문자열을 만들 수 있다.

# In[14]:


multiline = """Life is too short
You need python"""

print(multiline)


# 파이썬에서는 문자열도 더하거나 곱할 수 있다.

# In[15]:


a = 'Hello'
b = ' World'

a + b


# a라는 변수에 'Hello'라는 글자를, b라는 변수에 ' World'라는 글자를 입력한 후 두 변수를 더하면 두 글자가 합쳐진다.

# In[16]:


c = 'Quant'

c * 3


# 이번에는 c라는 변수에 'Quant'를 입력한 후 3을 곱하면, c가 세 번 반복된다.
# 
# #### f-string 포매팅
# 
# 문자열에서 특정 부분만이 바뀌고 나머지 부분은 일정할 경우, 파이썬에서는 f-string 포매팅을 이용해 매우 쉽게 나타낼 수 있다. (해당 기능은 파이썬 3.6 버전 이상부터 사용이 가능하다.)

# In[17]:


name = '이현열'
birth = '1987'

f'나의 이름은 {name}이며, {birth}년에 태어났습니다.'


# f-string의 형태는 **f'문자열 {변수} 문자열'** 이다. 즉 문자열 맨 앞에 f를 붙이면 f-string 포매팅이 선언되며, 중괄호 안에 변수를 넣으면 해당 부분에 변수의 값이 입력된다.
# 
# #### 문자열 길이 구하기
# 
# 문자열의 길이를 구할때는 `len()` 함수가 사용된다.

# In[18]:


a = 'Life is too short'
len(a)


# 'Life is too short'이라는 문장은 빈 칸을 포함하여 총 17 글자로 이루어져 있다.
# 
# #### 문자열 치환하기
# 
# 특정한 문자를 다른 문자로 바꾸는데는 `replace()` 함수가 사용된다.

# In[19]:


var = '퀀트 투자 포트폴리오 만들기'
var.replace(' ', '_')


# 먼저 var 변수에 '퀀트 투자 포트폴리오 만들기'라는 문자열을 입력했다. 그 후 `문자열.replace(a, b)` 메서드를 사용하면 문자열에서 a라는 문자를 b라는 문자로 바꿀 수 있다. 즉 ' '는 공백을 의미하여, 이러한 공백을 모두 밑줄(_)로 변경하였다.
# 
# #### 문자열 나누기
# 
# `split()` 메서드를 이용하면 문자열을 나눌 수 있다.

# In[20]:


var = '퀀트 투자 포트폴리오 만들기'
var.split(' ')


# `split()` 메서드 내부에 값을 입력하면, 해당 값을 기준으로 문자열을 나눠준다. 위 예제에서는 공백(' ')을 기준으로 각각의 단어를 나누었다.
# 
# #### 문자열 인덱싱과 슬라이싱
# 
# 인덱싱(Indexing)이란 문자열 중 특정 위치의 값을 가져오는 것이며, 슬라이싱(Slicing)이란 특정 위치가 아닌 범위에 해당하는 문자열을 가지고 오는 것이다.

# In[21]:


var = 'Quant'

var[2]


# 인덱싱과 슬라이싱은 대괄호([ ])를 사용해서 표현한다. `var[2]`란 두번째 문자를 의미하며, 이에 해당하는 'a'이 출력되었다. **참고로 파이썬은 숫자를 1이 아닌 0부터 세므로** 'Quant'에서 Q는 `var[0]`, u는 `var[1]`, a는 `var[2]`에 해당한다.
# 
# ```{table} 문자열의 순서
# :name: char_order
# |단어|Q|u|a|n|t|
# |---|---|---|---|---|---|
# |위치|0|1|2|3|4|5|
# ```

# In[22]:


var[-2]


# 인덱싱에 마이너스(-) 기호를 붙이면 문자열을 뒤에서부터 읽는다. 즉 `var[-2]`은 뒤에서 두번째 문자를 의미하며 이에 해당하는 'n'이 출력되었다.

# In[23]:


var[0:3]


# 슬라이싱은 [] 내부에 콜론(:) 기호를 사용하여 `시작:마지막`에 해당하는 문자를 출력한다. 즉 `var[0]` 부타 `var[3]`까지를 출력한다. 그런데 Quant에서 3에 해당하는 단어는 n임에도 불구하고 그 이전엔 Qua 까지만 출력이 되었다. 이는 슬리이싱에서 `var[시작:마지막]`을 지정할 때 마지막 번호에 해당하는 단어는 포함되지 않기 때문이며, `var[0:3]`은 0 이상 3 미만에 해당하는 문자만 출력한다.

# In[24]:


var[:2]


# 시작에 해당하는 부분을 명시하지 않으면 처음(0)부터 2 미만까지의 문자를 출력한다.

# In[25]:


var[3: ]


# 반대로 마지막에 해당하는 부분을 명시하지 않으면 3부터 마지막까지 문자를 출력한다.
# 
# ### 리스트
# 
# 파이썬에서는 연속된 데이터를 표현하기 위해 리스트(List) 자료형을 사용한다. 

# In[26]:


a = []
type(a)


# 리스트는 대괄호([ ])를 이용하여 생성할 수 있으며, 아무 값도 입력하지 않을 경우 빈 리스트가 생성된다.

# In[27]:


list_num = [1, 2, 3]
print(list_num)


# In[28]:


list_char = ['a', 'b', 'c']
print(list_char)


# In[29]:


list_complex = [1, 'a', 2]
print(list_complex)


# 리스트 내부에 각 요소는 쉼표(,)를 이용해 구분해준다. 요소값은 숫자(list_num), 문자열(list_char), 혹은 숫자와 문자열(list_complex)을 함께 가질 수도 있다.

# In[30]:


list_nest = [1, 2, ['a', 'b']]
print(list_nest)


# 혹은 리스트 자체를 하나의 요솟값으로 가질 수도 있다. 즉 리스트 안에는 어떠한 자료형도 들어갈 수 있다.
# 
# #### 리스트 인덱싱과 슬라이싱
# 
# 리스트도 문자열과 동일한 방법으로 인덱싱과 슬라이싱을 할 수 있다.

# In[31]:


var = [1, 2, ['a', 'b', 'c']]

var[0]


# 문자열과 동일하게 `var[0]`을 입력할 경우 해당 요소값인 1이 출력된다.

# In[32]:


var[2]


# `var[2]`를 입력할 경우 ['a', 'b', 'c']라는 리스트가 출력된다. 추가로 ['a', 'b', 'c'] 리스트에서 'a'라는 문자열만 추출하는 방법은 다음과 같다.

# In[33]:


var[2][0]


# 먼저 `var[2]`를 통해 ['a', 'b', 'c']를 추출하며, 뒤에 `[0]`을 추가적으로 붙여 첫번째 요소인 'a'가 출력된다. 이처럼 중첩된 리스트에서도 인덱싱은 여러번 하면 얼마든지 원하는 값을 선택할 수 있다. 이번에는 리스트의 슬라이싱에 대해서 살펴보자.

# In[34]:


var = [1, 2, 3, 4, 5]
var[0:2]


# 문자열의 슬라이싱과 동일하게 `var[0:2]`를 입력하면 리스트 a의 0 이상 2 미만에 해당하는 요소들이 출력된다.
# 
# #### 리스트 연산하기
# 
# 리스트도 `+`, `*` 연산을 제한적으로 사용할 수 있다. 

# In[35]:


a = [1, 2, 3]
b = [4, 5, 6]

a+b


# 리스트 사이에 `+` 기호를 사용하면 두 리스트를 하나로 합친다. 

# In[36]:


a = [1, 2, 3]
a * 3


# 리스트에 `*` 기호를 사용하면 해당 리스트를 n번 반복한다.
# 
# #### 리스트에 요소 추가하기
# 
# 다양한 방법을 통해 기존의 리스트에 새로운 데이터를 추가하거나 삽입할 수 있다.

# In[37]:


var = [1, 2, 3]
var.append(4)
print(var)


# `append()` 메서드는 기존의 리스트 맨 마지막에 데이터를 추가한다.

# In[38]:


var = [1, 2, 3]
var.append([4, 5])
print(var)


# 만약 `append()` 메서드 내에 리스트 형태를 입력할 경우 중첩된 형태로 데이터가 추가된다. 리스트에 새로운 리스트를 중첩된 형태가 아니라 리스트 형태로 확장하고 싶을 경우에는 `extend()` 메서드를 사용하면 된다.

# In[39]:


var = [1, 2, 3]
var.extend([4, 5])
print(var)


# `extend()` 메서드 내의 리스트인 [4, 5]가 중첩된 형태가 아니라 기존 데이터인 [1, 2, 3] 뒤에 확장이 되었다.
# 
# #### 리스트의 수정과 삭제
# 
# 인덱싱과 슬라이싱을 이용하면 리스트의 요소를 수정 혹은 삭제할 수 있다.

# In[40]:


var = [1,2,3,4,5]
var[2] = 10
print(var)


# 먼저 var라는 변수에 1부터 5까지 숫자로 구성된 리스트를 만들었다. 그 후 var의 두번재 요소에 10을 입력하면 해당 값으로 요소가 변경되었다.

# In[41]:


var[3] = ['a', 'b', 'c']
print(var)


# 이번에는 세번째 요소를 ['a', 'b', 'c']라는 요소로 변경하였다. 

# In[42]:


var[0 : 2] = ['가', '나']
print(var)


# 인덱싱을 이용해 데이터를 수정할 수도 있다. `var[0 : 2]`는 0 부터 1 까지의 데이터를 의미하며, 해당 데이터를 ['가', '나']로 변경하였다.
# 
# 이번에는 리스트에서 요소를 삭제하는 방법에 대해 살펴보겠으며, 먼지 `del` 명령어를 사용하는 방법에 대해 알아보자.

# In[43]:


var = [1, 2, 3]
del var[0]
print(var)


# `del 객체`를 이용하여 데이터를 삭제할 수 있다. 위의 예제에서 `del var[0]`는 var에서 영번째 요소를 삭제하라는 의미다. 인덱싱 뿐만 아니라 `dal var[0:2]`와 같이 슬라이싱을 통해서도 데이터를 삭제할 수 있다.

# In[44]:


var = [1, 2, 3]
var[0:1] = []
print(var)


# 슬라이싱을 통해 범위를 지정한 후 빈 리스트([])를 입력하여 해당 부분의 데이터를 삭제할 수도 있다.

# In[45]:


var = [1, 2, 3, 1, 2, 3]
var.remove(1)
print(var)


# `remove(x)` 메서드는 리스트에서 첫 번째로 나오는 x를 삭제하는 함수이다. 위 예제에서는 가장 먼저 나오는 1이 삭제된 것을 확인할 수 있다.

# In[46]:


var = [1, 2, 3]
var.pop()


# In[47]:


print(var)


# `pop()` 메서드는 리스트의 맨 마지막 요소를 반환하고 해당 요소는 삭제한다. 위 예에서 가장 마지막 요소인 3이 출력되고, var를 확인해보면 최종적으로 [1, 2]만 남아있다.
# 
# #### 리스트 정렬하기
# 
# 리스트 내의 데이터들은 `sort()` 메서드를 통해 정렬할 수 있다.

# In[48]:


var = [2, 4, 1, 3]
var.sort()
print(var)


# 1부터 4까지의 순서가 무작위로 존재했지만, `sort()`를 입력하면 오름차순으로 정렬된다.
# 
# ### 튜플
# 
# 튜플(Tuple) 자료형은 리스트와 매우 흡사하며 약간의 차이점만 있다. 먼저 리스트는 대괄호([ ])를 이용해 생성하지만 튜플은 소괄호(( ))를 이용해 생성한다. 또한 튜플은 값을 수정하거나 삭제할 수 없다.

# In[49]:


var = ()
type(var)


# 리스트와 마찬가지로 소괄호를 입력하면 빈 튜플이 생성된다.

# In[50]:


var = (1, )
print(var)


# 만일 값이 하나만 있을 경우에는 요소 뒤에 콤마(,)를 반드시 붙여야 한다.

# In[51]:


var = (1, 2, ('a', 'b'))
print(var)


# 튜플 역시 요소를 중첩하여 사용할 수 있다.

# In[ ]:


var = (1, 2)
del var[0]


# In[ ]:


---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
C:\Users\DOOMOO~1\AppData\Local\Temp/ipykernel_23248/2714829066.py in <module>
      1 var = (1, 2)
----> 2 del var[0]

TypeError: 'tuple' object doesn't support item deletion


# 만일 `del` 명령어를 이용해 요소값을 삭제하려고 할 경우 오류가 발생한다. 이처럼 튜플은 수정 혹은 삭제가 불가능하다.

# In[52]:


var = (1, 2, 3, 4, 5)
var[0]


# 인덱싱이나 슬라이싱의 경우 리스트와 동일하게 사용이 가능하다.
# 
# ### 딕셔너리
# 
# 딕셔너리(Dictionary)는 대응 관계를 나타내는 자료형으로써, 리스트나 튜플처럼 순서가 존재하지 않으며 대신 Key와 Value가 존재한다. 딕셔너리는 다음과 같은 형태를 가지고 있다.

# In[ ]:


{Key1:Value1, Key2:Value2, Key3:Value3, ...}


# 딕셔너리는 중괄호({ })를 감싸서 표현한다. 키(Key)-값(Value)의 형태로 데이터가 이루어져 있으며, 각각은 쉼표(,)로 구분된다. 예시를 살펴보도록 하자.

# In[53]:


var = {'key1' : 1, 'key2' : 2}
print(var)


# 키 값이 key1인 곳에는 1이라는 값이, 키 값이 key2인 곳에는 2라는 값이 딕셔너리 형태로 입력되었다.

# In[54]:


var = {'key1': [1, 2, 3], 'key2': ('a', 'b', 'c')}
print(var)


# 딕셔너리의 값에는 리스트나 튜플 형태도 입력이 가능하다.
# 
# #### Key를 사용해 Value 구하기
# 
# 문자열이나 리스트, 튜플의 경우 인덱싱이나 슬라이싱을 통해 요소값을 구할 수 있었지만, 딕셔너리는 순서가 존재하지 않으므로 이러한 방법을 사용할 수 없다. 딕셔너리는 Key를 사용해 이에 해당되는 Value를 얻을 수 있다.

# In[55]:


var = {'key1': 1, 'key2': 2, 'key3': 3}
var['key1']


# 먼저 var라는 변수에 딕셔너리를 입력한 후, `var['key1']`을 입력하면 딕셔너리 중 Key값이 key1에 해당하는 데이터의 Value를 반환한다. 즉 딕셔너리 변수에서 [ ] 안의 값은 순서를 뜻하는 것이 아니라 Key 값을 의미한다.
# 
# #### 쌍 추가하기 및 삭제하기
# 
# 기존 딕셔너리에 쌍을 추가하는 방법과 삭제하는 방법에 대해 살펴보자.

# In[56]:


var = {'key1': 1, 'key2': 2}
var['key3'] = 3
print(var)


# 먼저 key1과 key2로 이루어진 딕셔너리를 만들었다. 그 후 `var['key3'] = 3`을 입력하면 Key는 key3, Value는 3인 딕셔너리 쌍이 추가된다.

# In[57]:


del var['key1']
print(var)


# 리스트와 마찬가지로 딕셔너리에서도 `del` 명령어를 사용하면 해당 Key를 가진 딕셔너리 쌍이 삭제된다.
# 
# #### Key와 Value 구하기
# 
# 이번에는 딕셔너리의 Key와 Value를 한번에 구하는 법에 대해 살펴보자.

# In[58]:


var = {'key1': 1, 'key2': 2, 'key3': 3}
var.keys()


# `var.keys()`를 입력하면 var라는 딕셔너리에서 Key만을 모아 dict_keys 객체로 반환한다. 만일 이를 리스트 형태로 만들고자할 때는 다음과 같이 하면 된다.

# In[59]:


list(var.keys())


# 결과를 `list()`로 감싸주면 Key값이 리스트 형태로 출력된다.

# In[60]:


var.values()


# `var.values()`는 var라는 딕셔너리에서 Value만을 모아 dict_keys 객체로 반환한다.
# 
# ### 집합
# 
# 집합(Set)은 집합에 관련된 자료형이며, `set()` 키워드를 사용해 만들 수 있다. 집합 자료형의 특징으로는 중복을 허용하지 않는다는 점과, 순서가 없다는 점이다.

# In[61]:


set1 = set([1, 2, 3])
print(set1)


# `set()` 내에 리스트를 입력하면 집합이 만들어진다.

# In[62]:


set2 = set('banana')
print(set2)


# 반면 `set()` 내에 banana라는 단어를 입력했더니 'a', 'b', 'n'만 입력이 되었다. 이는 집합이 중복을 허용하지 않기 때문에 고유한 값만이 남았으며, 순서도 입력한 것과 다르다.
# 
# #### 합집합, 교집합, 차집합 구하기
# 
# 집합 자료형을 통해 합집합, 교집합, 차집합을 구해보도록 하자.
# 
# ```{figure} image/python/set.png
# ---
# name: set
# ---
# 집합 연산의 종류
# ```

# In[63]:


s1 = set([1, 2, 3, 4])
s2 = set([3, 4, 5, 6])


# 먼저 합집합을 구해보도록 하자. 합집합이란 하나에라도 속하는 원소들을 모두 모은 집합이다.

# In[64]:


s1.union(s2)


# `union()` 메서드를 사용하면 합집합을 구할 수 있다. 즉 1부터 6까지의 숫자가 집합에 입력되며, 두 집합에 공통으로 존재하는 3과 4는 한번만 입력이 된다.
# 
# 다음으로 교집합을 구해보도록 하자. 교집합이란 두 집합이 공통으로 포함하는 원소로 이루어진 집합이다.

# In[65]:


s1.intersection(s2)


# `intersection()` 메서드를 사용하면 교집합을 구할 수 있다. 즉 두 집합에 공통으로 존재하는 3과 4가 반환된다. 
# 
# 마지막으로 차집합을 구해보도록 하자. 차집합이란 집합 A에는 속하지만 집합 B에는 속하지 않는 원소들로 이루어진 집합이다.

# In[66]:


s1.difference(s2)


# `difference()` 메서드를 사용하면 집합 s1에서 교집합을 제외한 {1, 2}만이 반환된다.
# 
# ### 불리언
# 
# 불리언(Boolean) 자료형이란 참(True) 혹은 거짓(False)을 나타내는 자료형으로, 이 두가지 값만을 가질 수 있다. 참고로 True와 False는 첫 문자는 항상 대문자로 사용해야 한다.

# In[67]:


var = True
type(var)


# var 변수에 True를 입력한 후 타입을 확인해보면 bool, 즉 불리언 자료형임을 알 수 있다.

# In[68]:


1 == 1


# 파이썬에서 `==` 는 양측 값이 같은지를 확인하는 비교연산자이다. 좌측의 1과 우측의 1은 같으므로 True 즉 참이 반환된다.

# In[69]:


1 != 2


# `!=` 는 양측 값이 다른지를 확인하는 비교연산자이다. 좌측의 1과 우측의 2는 다르므로 역시나 True가 반환된다.
# 
# #### 자료형의 참과 거짓
# 
# 자료형 자체에도 참과 거짓이 존재한다.

# In[70]:


bool(0)


# `bool()` 함수는 참(True)과 거짓(False)을 반환하는 함수다. 숫자 0은 False에 해당한다.

# In[1]:


bool(1)


# In[2]:


bool(2)


# 반면 0이 아닌 숫자는 True에 해당한다.

# In[72]:


bool(None)


# None은 값의 부재를 나타내는데 사용되며, False에 해당한다.

# In[73]:


bool("")


# In[74]:


bool([])


# In[75]:


bool({})


# In[76]:


bool(())


# 문자열, 리스트, 딕셔너리, 튜플 등의 값이 비어 있을 경우는 False에 해당한다. 

# In[77]:


bool('Python')


# In[78]:


bool([1, 2, 3])


# In[79]:


bool({'Key':'Value'})


# In[80]:


bool((1, 2))


# 반면 데이터가 존재하면 True에 해당한다. 이를 요약하면 다음과 같다.
# 
# ```{table} 자료형의 참과 거짓
# :name: data_bool
# |값|True or False|
# |---|---|
# | 0 | False |
# | 0 외의 숫자 | True |
# | None | False |
# | "" | False |
# | [] | False |
# | {} | False |
# | () | False |
# | [데이터] | True |
# | {key:value} | True |
# | (데이터) | True |
# ```
# 
# ### 날짜와 시간
# 
# 날짜와 시간은 파이썬에서 기본으로 제공하는 자료형에는 포함되어 있지 않지만 데이터 분석을 할 때 빈번하게 다루는 자료형이다. 날짜와 시간과 관련된 패키지는 다음과 같다.
# 
# #### 날짜와 시간 구하기
# 
# `datetime` 패키지를 이용해 현재 날짜 및 시간 정보를 구할 수 있다.

# In[81]:


import datetime

var = datetime.datetime.now()
var


# In[82]:


type(var)


# `datetime` 클래스의 `now()` 메서드는 현재 날짜와 시간을 반환한다. 앞에서부터 [연도, 월, 일, 시, 분, 초, 마이크로초]를 의미한다. 이 중 연도에 해당하는 부분만 선택해보자.

# In[83]:


print(var.year)


# `var.` 뒤에 속성을 입력하면 이에 해당하는 값이 출력된다. 날짜와 시간과 관련된 속성은 다음과 같다.
# 
# - year: 연도
# - month: 월
# - day: 일
# - hour: 시
# - minute: 분
# - second: 초
# - microsecond: 마이크로초 (백만분의 일초)
# 
# 각 속성을 한번에 출력해보도록 하자.

# In[84]:


var.year, var.month, var.day, var.hour, var.minute, var.second, var.microsecond


# datetime 클래스에는 이 외에도 다양한 메서드가 존재한다. 

# In[85]:


var.weekday()


# `weekday`는 요일을 반환한다. 결과값으로 0은 월요일, 1은 화요일, 2는 수요일, 3은 목요일, 4은 금요일, 5는 토요일, 6은 일요일을 뜻한다.

# In[86]:


var.date(), var.time()


# `date()`는 날짜에 관련된 정보만, `time()`은 시간에 관련된 정보만 반환한다. 
# 
# #### 포맷 바꾸기
# 
# 포맷을 바꾸는데는 크게 두가지 메서드가 사용된다.
# 
# - `strftime`: 시간 정보를 문자열로 바꿈
# - `strptime`: 문자열을 시간 정보로 바꿈
# 
# 먼저 `strftime`를 이용해 시간 정보를 문자 정보로 바꿔보도록 하자.

# In[87]:


var


# 위의 시간 정보를 일반적으로 많이 사용하는 'yyyy-mm-dd', 즉 '연도-월-일' 형태로 바꿔보도록 하자.

# In[88]:


var.strftime('%Y-%m-%d')


# \%Y, \%m, \%d는 날짜 및 시간을 어떤 형식의 문자열로 만들지 결정하는 형식 문자열이다. 날짜 및 시간을 나타내는 형식은 다음과 같다.
# 
# ```{table} 날짜 및 시간 관련 포맷 코드
# :name: data_bool
# | 그룹 | 코드 | 뜻 |
# | --- | --- | --- |
# | 년 | %Y | 연도 (전체)  |
# |    | %y | 연도 (뒤 2자리만) |
# | 월 | %m | 월 |
# |    | %B | Locale 월 표현 (전체) |
# |    | %b | Locale 월 표현 (축약) |
# | 일 | %d | 일 |
# |    | %j | 연중 일 |
# | 시 | %H | 시 (24시간) |
# |    | %I | 시 (12시간) |
# |    | %p | Locale 오전, 오후 |
# | 분 | %M | 분 |
# | 초 | %S | 초 |
# | 마이크로초 | %f | 마이크로초 |
# | 요일 | %w | 요일 |
# | | %A | Locale 요일 (전체) |
# | | %a | Locale 요일 (축약형) |
# | 주 | %W | 연중 몇 번째 주인지 표현 (월요일 시작 기준) |
# | | %U | 연중 몇 번째 주인지 표현 (일요일 시작 기준) |
# | 날짜 표현 | %c | Locale 날짜와 시간 표현 |
# | | %x | Locale 날짜 표현 |
# | | %X | Locale 시간 표현 |
# ```
# 
# 예를 들어 시간 정보를 문자열로 바꿔보도록 하자.

# In[89]:


t = datetime.datetime(2022, 12, 31, 11, 59, 59)

t.strftime("%a %d, %b %y")


# In[90]:


t.strftime("%H시 %M분 %S초")


# 반대로 문자열로부터 날짜와 시간 정보를 읽은 후 `datetime` 클래스 객체로 만들 수 있으며, 이 경우 `strptime` 메서드를 사용한다. 

# In[91]:


datetime.datetime.strptime("2022-12-31 11:59:59", "%Y-%m-%d %H:%M:%S")


# 첫 번째 인자에 날짜와 시간 정보를 가진 문자열을, 두 번째 인자에 이에 해당하는 형식 문자열을 입력하면 `datetime` 클래스 객체로 변경된다.
# 
# #### 날짜와 시간 연산하기
# 
# 날짜 혹은 시간의 간격을 구할 수도 있다.

# In[92]:


dt1 = datetime.datetime(2022, 12, 31)
dt2 = datetime.datetime(2021, 12, 31)
td = dt1 - dt2

td


# 2022년 12월 31일에서 2021년 12월 31일을 빼면 days=365, 즉 365일의 차이가 있음을 확인할 수 있다. 이번에는 날짜에 특정 기간을 더해보도록 하자.

# In[93]:


dt1 = datetime.datetime(2021, 12, 31)
dt1 + datetime.timedelta(days = 1)


# `timedelta` 객체를 통해 원하는 기간을 더해거나 빼줄 수 있다. 2021년 12월 31일에 `days = 1`, 즉 1일을 더하면 다음날인 2022년 1월 1일이 계산된다. 그러나 `timedelta` 객체의 단점은 날짜와 초 단위로만 연산을 할 수 있다는 점이며, 월 단위의 경우 `dateutil` 패키지의 `relativedelta` 클래스를 이용하면 된다.

# In[94]:


from dateutil.relativedelta import relativedelta

dt1 + relativedelta(months = 1)


# `timedelta`와 사용법은 같으며, `months = 1`을 통해 한 달의 기간을 더할 수 있다.
# 
# #### 코드를 일시정지 하기
# 
# time 패키지의 `sleep()` 함수를 사용하면 일정 시간동안 프로세스를 일시정지할 수 있습니다.

# In[95]:


import datetime
import time

for i in range(3) :
    print(i)    
    print(datetime.datetime.now())
    print('-------')
    time.sleep(2)


# 위 코드는 0부터 2까지 for문 내에서 i와 현재 시간을 출력하며, `time.sleep(2)`을 통해 루프당 2초의 일시정지를 준다. 출력된 결과를 살펴보면 한 번의 루프가 끝난 후 약 2초 후에 다음 루프가 실행된 것을 확인할 수 있다.
# 
# ## 제어문
# 
# 파이썬 프로그래밍은 위에서부터 아래 방향으로 작성된 내용을 순서대로 실행한다. 반면 이러한 흐름을 제어하여 실행 순서를 바꾸거나 여러 번 반복하도록 하는 것이 제어문이다. 파이썬의 제어문에는 크게 if문, while문, for문이 있다.
# 
# ### if문
# 
# if문, 혹은 조건문이란 입력된 조건을 판단하여 해당 조건에 맞는 상황을 실행한다. if문의 기본적인 구조는 다음과 같다.

# In[ ]:


if 조건:
    실행


# 1. `if`를 통해 if문을 선언하고, 바로 뒤에 조건을 입력한 후 콜론(:)을 붙인다.
# 2. 줄바꿈을 해준 후 만일 조건이 True일 경우 실행할 코드를 입력한다. 이 때 조건문 바로 아래부터는 if문에 속하는 문장이므로 들여쓰기를 해주어야 하며, 공백을 4번 입력하거나 탭을 누른다. 만일 들여쓰기가 제대로 되지 않을 경우 오류가 발생한다. 
# 
# 예를 살펴보도록 하자.

# In[96]:


x = 2

if x > 0:
    print('값이 0보다 큽니다.')


# 1. 먼저 x라는 변수에 2라는 숫자를 입력한다.
# 2. `if`를 통해 조건을 선언하며 조건에는 `x > 0`을 설정한 후 콜론을 입력한다.
# 3. 만일 위 조건이 True일 경우 '값이 0보다 큽니다.'를 출력한다.
# 
# 실제 결과를 살펴보다 2는 0보다 크므로 해당 문장이 출력된다.

# In[97]:


x = -1

if x > 0:
    print('값이 0보다 큽니다.')


# 반면 위의 경우 코드를 실행해도 아무런 결과가 나타나지 않는다. 이는 x에 입력된 -1이 0보다 작으므로 조건이 False이기 때문이다. 이처럼 조건문이 False일 실행할 상황은 `else`를 이용한다.

# In[ ]:


if 조건:
    실행 1
else:
    실행 2


# 만일 조건이 True일 경우에는 [실행 1]에 해당하는 코드가 실행되지만, 그렇지 않을 경우 [실행 2]에 해당하는 코드가 실행된다. `if`와 마찬가지로 `else`문 아래의 문장도 들여쓰기를 해주어야 한다.

# In[1]:


x = -1

if x > 0:
    print('값이 0보다 큽니다.')
else:
    print('값이 음수입니다.')


# -1이 0보다 작으므로 조건은 False다. 따라서 else에 속하는 '값이 음수입니다.'가 출력된다. 만일 조건이 여러개인 다중 조건을 판단하려면 `if`와 `else` 사이에 `elif`를 추가하면 된다.

# In[ ]:


if 조건 1:
    실행 1
elif 조건 2:
    실행 2
elif 조건 3:
    실행 3
...
else:
    실행 n


# `if`의 [조건 1]이 False일 경우 바로 아래의 `elif`를 통해 [조건 2]를 판단한다. 만일 [조건 2]가 True일 경우에는 [실행 2]에 해당하는 코드가 실행되지만, False일 경우에는 다시 [조건 3]을 판단한다. 만일 모든 `elif`의 조건이 False일 경우 최종적으로 [실행 n]에 해당하는 코드가 실행되며, `elif`는 개수에 제한 없이 사용할 수 있다.

# In[2]:


x = 3

if x >= 10:
    print('값이 10보다 큽니다.')
elif x >= 0:
    print('값이 0 이상 10 미만입니다.')
else:
    print('값이 음수입니다.')


# 먼저 `if` 조건에서 3은 10 보다 크지 않으므로 조건이 False이며, 이에 해당하는 코드가 실핻되지 않는다. 그 후 `elif` 조건에서 3은 0보다 크므로 이에 해당하는 코드인 '값이 0 이상 10 미만입니다.'가 출력된다.
# 
# 만일 조건문이 `if`와 `else`로만 구성될 경우 다음과 같이 간단하게 작성할 수도 있다.

# In[ ]:


[조건문이 True인 경우] if 조건문 else [조건문이 False 경우]


# 예제를 살펴보도록 하자.

# In[3]:


x = 7

'0 이상' if x >= 0 else '음수'


# x가 0 이상일 경우에는 '0 이상'을 출력하며, 그렇지 않을 경우엔 '음수'를 출력한다. 이처럼 조건부 표현식은 한 줄로 작성할 수 있어 훨씬 가독성이 좋다.
# 
# ### while문
# 
# while문, 혹은 반복문은 특정 조건을 만족하는 동안 반복해서 코드를 실행한다. while문의 기본적인 구조는 다음과 같다.

# In[ ]:


while 조건:
    실행


# [조건]에 해당하는 부분이 True인 동안에는 [실행]에 해당하는 코드가 반복해서 수행된다. while문도 if문과 마찬가지로 [실행]에 해당하는 부분은 들여쓰기를 해주어야 한다. 예제를 살펴보도록 하자.

# In[4]:


num = 1

while num < 5:
    print(num)
    num = num + 1


# 1. 먼저 num에 1을 입력한다.
# 2. 만일 num이 5 미만일 경우 아래의 코드를 계속해서 수행한다.
# 3. num을 출력한다.
# 4. num에 1을 더한다.
# 
# 1부터 4까지 숫자가 출력되다가, num이 5가 된 순간에는 while문의 조건이 False 이므로 코드 실행이 종료된다. 만약 `num = num + 1` 부분이 없다면 num은 계속 1인 상태이므로 `print(num)`이 무한대로 실행된다.
# 
# `while`문 내부에 `if`문을 추가할 수도 있다.

# In[5]:


num = 1

while num < 10 :
    if num % 2 == 0 :
        print(f'{num}은 짝수입니다.')    
    num = num + 1


# 1. num에 1을 입력한다.
# 2. `while`을 통해 num이 10 미만일 경우 아래의 코드를 계속해서 수행한다.
# 3. `if`를 추가하여 num % 2 == 0일 경우, 즉 나머지가 0일 경우 글자를 출력한다.
# 4. num에 1을 더한다.
# 
# 즉 1부터 9까지 숫자 중, 짝수인 부분만 글자를 출력한다. 만일 코드가 계속해서 실행되다가 특정 조건을 만족할 경우 멈추게 하고 싶을 경우 if문에 `break`를 사용하면 된다.

# In[6]:


money = 1000

while True:        
    money = money - 100
    print(f'잔액은 {money}원 입니다.')
    
    if money <= 0 : 
        break


# 1. money에 1000을 입력한다.
# 2. `while True`를 통해 코드가 무한히 반복된다.
# 3. money에서 100을 빼준 후, 잔액을 출력한다.
# 4. if문을 통해 잔액이 0 미만일 경우 `break`를 통해 while문을 멈춘다.
# 
# 결과를 살펴보면 잔액이 100원씩 줄어들다가 0원이 된 순간, if문의 조건이 True이므로 break를 통해 while문이 멈추게 된다.
# 
# ### for문
# 
# for문은 while문과 동일한 반복문이지만, 무한히 반복되는 것이 아닌 특정 횟수만큼만 반복되는 특징이 있다. for문의 기본적인 구조는 다음과 같다.

# In[ ]:


for 변수 in 리스트(또는 튜플, 문자열):
    실행


# 리스트 또는 튜플, 문자열의 첫 번째 요소부터 마지막 요소까지 차례로 변수에 대입된 후 [실행]에 해당하는 코드가 실행되며, 역시나 들여쓰기를 해야한다. 예제를 살펴보도록 하자.

# In[104]:


var = [1, 2, 3]

for i in var:
    print(i)


# var에 해당하는 [1, 2, 3]의 리스트 중 첫 번째 요소인 1이 먼저 변수 i에 대입된 후 `print(i)`가 실행된다. 그 후 두 번째 요소인 2가 다시 변수 i에 대입되어 `print(i)`가 실행되고, 리스트의 마지막 요소까지 반복된다. 
# 
# for문 역시 if문과 함께 사용할 수 있다.

# In[105]:


var = [10, 15, 17, 20]

for i in var:
    if i % 2 == 0:
        print(f'{i}는 짝수입니다.')
    else:
        print(f'{i}는 홀수입니다.')


# 1. var에 [10, 15, 17, 20]를 입력한다.
# 2. for문을 통해 var의 요소를 하나씩 i에 대입하여 아래의 코드들을 실행한다.
# 3. if문을 통해 만일 나머지가 0일 경우 '짝수입니다.'라는 글자를, 그렇지 않을 경우 else를 통해 '홀수입니다.'라는 글자를 출력한다.
# 
# `for`문은 `range()` 함수와 함께 쓰이는 경우가 많다. `range()` 함수는 숫자(정수) 리스트를 자동으로 만들어준다. 

# In[106]:


range(10)


# `range()` 함수 내에 10을 입력할 경우 0부터 10 미만의 숫자에 해당하는 range 객체를 만들어 준다.

# In[107]:


range(5, 10)


# 시작과 끝 숫자를 지정할 수도 있다. `range(5, 10)`을 입력하면 5부터 10 미만의 숫자에 해당하는 range 객체를 만들어 준다. `range()` 함수의 예시를 살펴보도록 하자.

# In[108]:


for i in range(5):
    print(i)


# `range(5)`는 0부터 5 미만의 숫자 리스트를 의미하며, for문을 통해 요소를 하나씩 출력하였다.
# 
# 리스트 안에 `for`문을 포함하는 리스트 내포(List Comprehension)을 사용하면 더욱 직관적인 코딩이 가능하다.

# In[109]:


a = [1, 2, 3]


# 만일 위 값들의 제곱을 구하려면 어떻게 해야할까? 일반적인 `for`문을 사용한 코드는 다음과 같다.

# In[110]:


result = []

for i in a:
    result.append(i**2)

print(result)


# 1. 빈 리스트(result)를 만든다.
# 2. i에 요소를 하나씩 입력하여 제곱(`i**2`)을 구한 후, append를 이용해 리스트에 추가한다.
# 3. 결과를 확인해보면 모든 요소의 제곱이 구해졌다.
# 
# 그러나 리스트 내포 안에 `if` 조건을 사용하면 위 코드를 훨씬 간단하게 나타낼 수 있다. 리스트 내포의 문법은 다음과 같다.

# In[ ]:


[실행 for 변수 in 리스트(또는 튜플, 문자열)]


# 이는 기존의 `for`문에서 위아래를 변경한 후, 리스트 내에 넣어 표현한 것이다. 실제 코드로 나타내면 다음과 같다.

# In[111]:


result = [i**2 for i in a]
print(result)


# 리스트 내포를 사용할 경우 기존의 for문에 비해 훨씬 간단하게 표현할 수 있다.
# 
# ### 오류에 대한 예외처리
# 
# `for`문을 실행하던 중 오류가 발생하면 작업이 끊겨 루프를 처음부터 다시 실행해야 한다. 대상이 얼마되지 않는다면 큰 문제가 되지 않겠지만, 수십분 혹은 몇시간이 걸리는 작업을 하던 중 오류가 발생해 작업을 처음부터 다시 해야하는 것은 매우 비효율적이다. `try-except`문을 이용하면 예외처리, 즉 오류가 발생할 경우 이를 무시하고 넘어갈 수 있다.
# 
# `try-except`문의 구조는 다음과 같다.

# In[ ]:


try:
    expr
except:
    error-handler-code
else:
    running-code
finally:
    cleanup-code


# 1. try 내의 `expr`는 실행하고자 하는 코드를 의미한다.
# 2. except 내의 `error-handler-code`는 오류 발생 시 실행할 코드를 의미한다.
# 3. else 내의 `running-code`는 expr 코드가 문제가 없을 경우 실행되는 코드, finally 내의 `cleanup-code` 코드는 오류 여부와 관계 없이 무조건 수행할 구문을 의미하며, 이 둘은 생략할 수도 있다.
# 
# 예제를 통해 살펴보도록 하자. 

# In[9]:


number = [1, 2, 3, "4", 5]


# 먼저 number 변수에는 1에서 5까지 값이 입력되어 있으며, 다른 값들은 형태가 숫자인 반면 4는 문자 형태다.

# In[ ]:


for i in number:
    print(i ** 2)


# In[ ]:


---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
~\AppData\Local\Temp/ipykernel_24668/914548984.py in <module>
----> 1 for i in number:
      2     print(i **2)

NameError: name 'number' is not defined


# `for`문을 통해 순서대로 값들의 제곱을 출력하는 명령어를 실행하면 '문자 4'는 제곱을 할 수 없어 오류가 발생한다. `try-except`문을 사용하면 이처럼 오류가 발생하는 루프를 무시하고 다음 루프로 넘어갈 수 있다.

# In[10]:


for i in number:
    try:
        print(i ** 2)
    except:
        print('Error at: ' + i)


# expr 부분은 `print(i ** 2)`이며, error-handler-code 부분은 오류가 발생한 i를 출력한다. 해당 코드를 실행하면 문자 4에서 오류가 발생함을 알려준 후 루프가 멈추지 않고 다음으로 진행된다.
# 
# ### `tqdm()` 함수를 이용한 진행 단계 확인하기
# 
# `for`문의 시간이 오래 걸리는 작업의 경우 어느정도 진행되었는지 궁금할 때가 있다. 파이썬에서는 tqdm 패키지를 통해 진행 정도를 손쉽게 확인할 수 있다.

# In[12]:


import time
from tqdm import tqdm

for i in tqdm(range(10)):
    time.sleep(0.1)


# tqdm 패키지에서 `tqdm()` 함수를 불러온 뒤, `for`문의 loop에 해당하는 부분을 `tqdm()` 로 감싸주면, 진행 정도를 확인할 수 있다.
# 
# ## 함수
#  
# 중고등학교 수학시간에 우리는 함수라는 개념을 배웠다. $y=f(x)$라는 수식이 있을 때 $x$라는 값을 $f()$라는 함수에 입력하면 $y$라는 결과값이 나온다. 예를 들어 다음과 같은 함수가 있다고 생각해보자.
# 
# $$y = 2x + 1$$
# 
# 만일 $x$에 1을 넣으면 결과는 $2×1 + 1 = 3$ 이며, $x$에 2를 넣으면 결과는 $2×2 + 1 = 5$ 이다.
# 
# ```{figure} image/python/fun.png
# ---
# name: fun
# ---
# 함수
# ```
# 
# 프로그래밍에서의 함수도 이와 비슷하다. 어떠한 입력값을 함수에 넣으면 이를 토대로 코드가 돌아가고, 그 결과를 반환한다. 함수를 사용하는 이유는 중복된 코드를 계속해서 작성하지 않기 위해서다. 만일 반복적으로 사용하는 코드가 있다면 이를 매번 적기 보다는 함수로 만들어두고, 필요할 때마다 함수를 사용하는 것이 효과적이다. 
# 
# 우리는 앞서 `print()`와 같이 수많은 함수를 이미 사용했다. 이처럼 가장 이상적인 방법은 기존에 누군가 작성한 패키지 혹은 함수를 찾아 이용하는 것이지만, 그렇지 못할 경우에도 나만의 함수를 쉽게 만들어 사용할 수 있다. 파이썬에서 함수를 만드는 법은 다음과 같다.

# In[ ]:


def f(x):
    statement
    return y


# 1. def 키워드를 통해 함수임을 선언한다.
# 2. f는 함수명을 뜻한다.
# 3. x는 함수에 들어가는 매개변수(Parameter)를 뜻한다.
# 4. 줄을 바꾼 후 들여쓰기를 한다.
# 5. statement에 해당하는 코드가 실행된다.
# 6. return 뒤에 적은 y가 반환되며, 함수가 종료된다.
# 
# 예시로 제곱근을 계산하는 함수를 만들어보자.

# In[13]:


def sqrt(x):
    res = x**(1 / 2)
    return res


# In[116]:


sqrt(4)


# In[117]:


sqrt(9)


# 1. def를 통해 함수를 선언하며, 함수명은 sqrt로 한다.
# 2. 매개변수는 x 하나가 사용된다.
# 3. x ** (1/2)은 $x^{\frac{1}{2}}$를 뜻하며, 즉 제곱근을 구한다. 이를 res라는 변수에 저장한다.
# 4. 최종적으로 res를 반환한다.
# 
# 만들어진 함수에 4와 9라는 숫자를 넣으면 각각의 제곱근인 2와 3을 출력된다. 참고로 함수에 입력한 4와 9처럼 함수를 호출할 때 전달하는 입력값은 인자(Argument) 혹은 인수라 한다. 
# 
# 이번에는 매개변수가 여러개인 함수를 만들어보도록 하자.

# In[118]:


def multiply(x, y):
    res = x**y
    return res


# In[119]:


multiply(x = 3, y = 4)


# In[120]:


multiply(5, 2)


# 매개변수로 x와 y 두개가 사용되었으며, $x^y$를 구하는 함수인 `multiply()`를 만들었다. `multiply(x = 3, y = 4)`와 같이 각 매개변수에 대응되는 인자를 직접 지정할 수도 있지만, `multiply(5, 2)`와 같이 인자만 입력하면 함수에서 정의한 순서에 따라 x에는 5, y에는 2가 대입되어 계산이 된다.

# In[121]:


def divide(x, n=2):
    res = x / n
    return (res)


# In[122]:


divide(3)


# In[123]:


divide(6, 3)


# 이번에는 매개변수 부분에 `n = 2`를 통해 디폴트 값을 설정하였다. 즉 n에 해당하는 부분에 값을 입력하지 않을 경우 n에는 2라는 값이 자동으로 입력된다.
# 
# 위 함수에서는 매개변수가 'x', 'n' 2개가 필요함에도 불구하고 `divide(3)`은 1.5라는 값이 계산되었다. 즉 x에는 3이라는 값이 입력되었지만, n에는 값이 입력되지 않아 디폴트 값인 2가 들어갔으며, 3/2의 결과인 1.5가 계산된다. 반면 `divide(6, 3)`의 경우 n에 3이라는 값을 입력하였으므로 6/3의 결과인 2가 계산되었다.
# 
# #### 람다 함수
# 
# `if`문이나 `for`문을 한 줄로 간단하게 나타냈던 것과 같이, 람다(lambda)를 이용하면 간단하게 함수를 만들 수 있다. 람다의 사용법은 다음과 같다.

# In[ ]:


함수명 = lambda 매개변수1, 매개변수2, ...: statement


# 예제로 나눗셈을 하는 함수를 람다를 통해 만들어보도록 하자.

# In[126]:


divide_lam = lambda x, n: x / n

divide_lam(6, 3)


# 위에서 def를 통해 만든 함수 `divide()`와 결과가 동일하다. 또한 람다를 통해 만든 함수는 return 명령어가 없어도 결괏값을 반환한다.
