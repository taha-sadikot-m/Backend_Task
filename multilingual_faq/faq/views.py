from rest_framework.response import Response
from rest_framework.views import APIView
from .models import FAQ
from .serializers import FAQSerializer  # You need to create this serializer

class FAQListView(APIView):
    def get(self, request, *args, **kwargs):
        lang = request.GET.get('lang', 'en')  # Default to English
        faqs = FAQ.objects.all()

        for faq in faqs:
            if lang == 'hi':
                faq.question = faq.question_hi or faq.question
                faq.answer = faq.answer_hi or faq.answer
            elif lang == 'bn':
                faq.question = faq.question_bn or faq.question
                faq.answer = faq.answer_bn or faq.answer

        serializer = FAQSerializer(faqs, many=True)
        return Response(serializer.data)
