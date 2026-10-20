import os
import replicate

class VideoAgent:
    def __init__(self, name="VideoAgent"):
        self.name = name
        self.api_token = os.environ.get("REPLICATE_API_TOKEN")
        if not self.api_token:
            print("⚠️ تنبيه: لم يتم العثور على REPLICATE_API_TOKEN في متغيرات البيئة.")

    def generate_video(self, prompt_text: str, visual_prompt: str = None, **kwargs):
        """
        إرسال طلب توليد فيديو سينمائي إلى منصة Replicate
        """
        # استخدام visual_prompt إذا تم تمريره، وإلا استخدام prompt_text
        final_prompt = visual_prompt if visual_prompt else prompt_text

        print(f"🎬 [{self.name}] جاري إرسال طلب الفيديو إلى Replicate بناءً على الوصف: '{final_prompt}'...")

        if not self.api_token:
            print("⚠️ مفتاح REPLICATE_API_TOKEN غير معرف، سيتم محاكاة التوليد أو إيقاف الطلب.")
            # يمكنك إرجاع رابط وهمي للتجربة إذا لم تضف الـ Secret بعد، أو رفع خطأ
            return "https://replicate.delivery/mock-video-output.mp4"

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

def generate_cinematic_video(prompt_text: str):
    agent = VideoAgent()
    return agent.generate_video(prompt_text)

if __name__ == "__main__":
    sample_prompt = "A cinematic shot of a futuristic cyberpunk city at night, neon lights reflecting on wet streets, 4k resolution, hyperrealistic."
    generate_cinematic_video(sample_prompt)
