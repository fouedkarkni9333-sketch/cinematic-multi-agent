import os
import urllib.request
import asyncio
import replicate
import edge_tts

class VideoAgent:
    def __init__(self, name="VideoAgent"):
        self.name = name
        self.api_token = os.environ.get("REPLICATE_API_TOKEN")
        if not self.api_token:
            print("⚠️ تنبيه: لم يتم العثور على REPLICATE_API_TOKEN في متغيرات البيئة.")

    async def _generate_speech_audio(self, text: str, output_audio_path: str = "temp_voice.mp3"):
        """
        توليد صوت ناطق عالي الجودة ومجاني 100% بدون أي مفاتيح مدفوعة
        """
        print(f"🎙️ [{self.name}] جاري تحويل النص إلى صوت سينمائي/كرتوني مجاناً...")
        voice = "ar-EG-SalmaNeural" if any("\u0600" <= c <= "\u06FF" for c in text) else "en-US-ChristopherNeural"
        communicate = edge_tts.Communicate(text, voice)
        await communicate.save(output_audio_path)
        return output_audio_path

    def generate_video(self, prompt_text: str = None, visual_prompt: str = None, dialogue_text: str = None, **kwargs):
        """
        توليد مشهد كرتوني أنيميشن احترافي مع توليد الصوت الخاص به مجاناً
        """
        raw_prompt = prompt_text if prompt_text else (visual_prompt if visual_prompt else "A vibrant animated cartoon character talking in a expressive colorful background")
        
        # تحسين الوصف ليكون كرتونياً وأنيميشن بصورة حيوية
        cartoon_prompt = f"Vibrant 3D animated cartoon scene, expressive character movement, Pixar and Disney anime style, highly detailed animation, vivid colors, {raw_prompt}"

        print(f"🎬 [{self.name}] جاري إرسال طلب المشهد الكرتوني إلى Replicate: '{cartoon_prompt}'...")

        if not self.api_token:
            print("⚠️ مفتاح REPLICATE_API_TOKEN مفقود!")
            raise ValueError("مفتاح REPLICATE_API_TOKEN مفقود في GitHub Secrets.")

        try:
            # 1. توليد مشهد الحركة الكرتونية من Replicate
            video_url = replicate.run(
                "minimax/video-01",
                input={
                    "prompt": cartoon_prompt,
                    "prompt_optimizer": True
                }
            )
            print(f"✅ تم بنجاح استلام رابط الفيديو المرئي: {video_url}")

            # 2. توليد الصوت المرتبط بالمشهد مجاناً
            speech_text = dialogue_text if dialogue_text else raw_prompt
            audio_path = asyncio.run(self._generate_speech_audio(speech_text))
            print(f"✅ تم إنشاء ملف الصوت الناطق بنجاح: {audio_path}")

            return video_url

        except Exception as e:
            print(f"❌ حدث خطأ أثناء توليد الفيديو والصوت: {e}")
            raise e

def generate_cinematic_video(prompt_text: str = "A cheerful cartoon hero talking excitedly", dialogue_text: str = None):
    agent = VideoAgent()
    return agent.generate_video(prompt_text=prompt_text, dialogue_text=dialogue_text)

if __name__ == "__main__":
    sample_prompt = "A cute 3D animated robot talking cheerfully in a colorful futuristic cartoon station"
    sample_dialogue = "مرحباً بكم في عالم الرسوم المتحركة والذكاء الاصطناعي!"
    generate_cinematic_video(prompt_text=sample_prompt, dialogue_text=sample_dialogue)
