from django import forms
from pybo.models import Question, Answer

# 모델 폼을 상속. 장고에는 일반 폼(forms.Form)과 모델 폼(forms.ModelForm)이 존재
# 모델 폼의 경우 이너 클래스인 Meta 클래스가 반드시 필요. Meta 클래스에 사용할 모델 및 속성을 지정
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question # 사용할 모델
        fields = ['subject', 'content'] # QuestionForm에서 사용할 Question 모델의 속성
        # widgets = {
        #     'subject':forms.TextInput(attrs={'class':'form-control'}),
        #     'content':forms.Textarea(attrs={'class':'form-control', 'rows':10}),
        # } # 부트스트랩을 적용하기 위한 방법. form.as_p가 HTML 코드를 자동생성하므로 부트스트랩을 적용할 수 없기 때문
        labels = {
            'subject':'제목',
            'content':'내용',
        } # 화면 상의 표시 내용을 바꾸는 방법.

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content':'답변내용',
        }