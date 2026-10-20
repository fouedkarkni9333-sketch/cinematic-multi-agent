import os
import replicate

class VideoAgent:
    def __init__(self, name="VideoAgent"):
        self.name = name
        self.api_token = os.environ.get("REPLICATE_API_TOKEN")
        if not self.api_token:
            print("⚠️ تنبيه: لم يتم العثور على REPLICATE_API_TOKEN في متغيرات البيئة.")

    def generate_video(self, prompt_text: str = None, visual_prompt: str = None, **kwargs):
        """
        إرسال طلب توليد فيديو سينمائي إلى منصة Replicate مع دعم كافة احتمالات الاستدعاء
        """
        # اختيار النص المتاح أياً كان اسم المعامل المرسل من main.py
        final_prompt = prompt_text if prompt_text else (visual_prompt if visual_prompt else "Cinematic masterpiece, highly detailed, 4k")

        print(f"🎬 [{self.name}] جاري إرسال طلب الفيديو إلى Replicate بناءً على الوصف: '{final_prompt}'...")

        if not self.api_token:
            print("⚠️ مفتاح REPLICATE_API_TOKEN غير معرف في Secrets!")
            raise ValueError("مفتاح REPLICATE_API_TOKEN مفقود في GitHub Secrets.")

        try:
            output = replicate.run(
                "minimax/video-01",
                input={
                    "prompt": final_prompt,
                    "prompt_optimizer": True
                }
            )
            print(f"✅ تم بنجاح استلام رابط الفيديو الناتج: {output}")
            return output
        except Exception as e:
            print(f"❌ حدث خطأ أثناء توليد الفيديو: {e}")
            raise e

def generate_cinematic_video(prompt_text: str = "Cinematic scene"):
    agent = VideoAgent()
    return agent.generate_video(prompt_text=prompt_text)

if __name__ == "__main__":
    sample_prompt = "A cinematic shot of a futuristic cyberpunk city at night, neon lights reflecting on wet streets, 4k resolution, hyperrealistic."
    generate_cinematic_video(sample_prompt)
