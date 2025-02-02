from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator

translator = Translator()

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()

    # Hindi translations
    question_hi = models.TextField(blank=True, null=True)
    answer_hi = RichTextField(blank=True, null=True)

    # Bengali translations
    question_bn = models.TextField(blank=True, null=True)
    answer_bn = RichTextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # Hindi translation
        if not self.question_hi or self.question_hi.strip() == "":
            try:
                self.question_hi = translator.translate(self.question, dest='hi').text
            except Exception as e:
                print(f"Translation failed for question in Hindi: {e}")

        if not self.answer_hi or self.answer_hi.strip() == "":
            try:
                self.answer_hi = translator.translate(self.answer, dest='hi').text
            except Exception as e:
                print(f"Translation failed for answer in Hindi: {e}")

        # Bengali translation
        if not self.question_bn or self.question_bn.strip() == "":
            try:
                self.question_bn = translator.translate(self.question, dest='bn').text
            except Exception as e:
                print(f"Translation failed for question in Bengali: {e}")

        if not self.answer_bn or self.answer_bn.strip() == "":
            try:
                self.answer_bn = translator.translate(self.answer, dest='bn').text
            except Exception as e:
                print(f"Translation failed for answer in Bengali: {e}")

        super().save(*args, **kwargs)
