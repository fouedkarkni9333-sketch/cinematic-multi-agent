import os
import time
import replicate

class VideoAgent:
    def __init__(self):
        self.api_token = os.environ.get("REPLICATE_API_TOKEN")
        if not self.api_token:
            print("⚠️ تنبيه: لم يتم العثور على REPLICATE_API_TOKEN في متغيرات البيئة.")

    def generate_video(self, prompt_text: str):
        """
        إرسال طلب توليد فيديو سينمائي إلى منصة Replicate
        """
        if not self.api_token:
            raise ValueError("مفتاح REPLICATE_API_TOKEN غير معرف!")

        print(f"🎬 جاري إرسال طلب الفيديو إلى Replicate بناءً على الوصف: '{prompt_text}'...")

        try:
            output = replicate.run(
                "minimax/video-01",
                input={
                    "prompt": prompt_text,
                    "prompt_optimizer": True
                }
            )
            print(f"✅ تم بنجاح استلام رابط الفيديو الناتج: {output}")
            return output
        except Exception as e:
            print(f"❌ حدث خطأ أثناء توليد الفيديو: {e}")
            raise e

def generate_cinematic_video(prompt_text: str):
    agent = VideoAgent()
    return agent.generate_video(prompt_text)

if __name__ == "__main__":
    sample_prompt = "A cinematic shot of a futuristic cyberpunk city at night, neon lights reflecting on wet streets, 4k resolution, hyperrealistic."
    generate_cinematic_video(sample_prompt)
