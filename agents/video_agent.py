import os
import urllib.request
import asyncio
import replicate
import edge_tts
from moviepy.editor import VideoFileClip, AudioFileClip

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
        # صوت عربي/إنجليزي تعبيري احترافي مجاني
        voice = "ar-EG-SalmaNeural" if any("\u0600" <= c <= "\u06FF" for c in text) else "en-US-ChristopherNeural"
        communicate = edge_tts.Communicate(text, voice)
        await communicate.save(output_audio_path)
        return output_audio_path

    def generate_video(self, prompt_text: str = None, visual_prompt: str = None, dialogue_text: str = None, **kwargs):
        """
        توليد مشهد كرتوني أنيميشن متكامل مع دمج الصوت مجاناً
        """
        raw_prompt = prompt_text if prompt_text else (visual_prompt if visual_prompt else "A vibrant animated cartoon character talking in a expressive colorful background")
        
        # تحسين الوصف ليكون كرتونياً وأنيميشن بصورة احترافية حيوية
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
            print(f"✅ تم استلام رابط الفيديو المرئي: {video_url}")

            # 2. تنزيل فيديو المشهد مؤقتاً
            raw_video_path = "raw_video.mp4"
            urllib.request.urlretrieve(str(video_url), raw_video_path)

            # 3. توليد الصوت مجاناً إذا كان هناك حوار أو استخدام النص لوصف الصوت
            speech_text = dialogue_text if dialogue_text else raw_prompt
            audio_path = asyncio.run(self._generate_speech_audio(speech_text))

            # 4. دمج الصوت مع الفيديو مجاناً بدون أي خوادم مدفوعة
            print(f"🎬 [{self.name}] جاري دمج الصوت مع المشهد الكرتوني...")
            video_clip = VideoFileClip(raw_video_path)
            audio_clip = AudioFileClip(audio_path)

            # ضبط طول الصوت ليتناسب مع الفيديو
            final_audio = audio_clip.subclip(0, min(video_clip.duration, audio_clip.duration))
            final_video = video_clip.set_audio(final_audio)

            output_final_path = "final_cartoon_video.mp4"
            final_video.write_videofile(output_final_path, codec="libx264", audio_codec="aac", logger=None)

            # إغلاق المقاطع لتحرير الذاكرة
            video_clip.close()
            audio_clip.close()

            print(f"✨ تم إنتاج المشهد الكرتوني الناطق بنجاح وحفظه في: {output_final_path}")
            return output_final_path

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
