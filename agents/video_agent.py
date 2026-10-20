import os
import urllib.request
import asyncio
import subprocess
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
        توليد صوت ناطق مجاني 100% باستخدام edge-tts
        """
        print(f"🎙️ [{self.name}] جاري تحويل النص إلى صوت مجاناً...")
        voice = "ar-EG-SalmaNeural" if any("\u0600" <= c <= "\u06FF" for c in text) else "en-US-ChristopherNeural"
        communicate = edge_tts.Communicate(text, voice)
        await communicate.save(output_audio_path)
        return output_audio_path

    def generate_video(self, prompt_text: str = None, visual_prompt: str = None, dialogue_text: str = None, **kwargs):
        """
        توليد مشهد كرتوني ودمج الصوت تلقائياً مجاناً (0 مليم)
        """
        raw_prompt = prompt_text if prompt_text else (visual_prompt if visual_prompt else "A vibrant animated cartoon character talking cheerfully")
        cartoon_prompt = f"Vibrant 3D animated cartoon scene, expressive character movement, Pixar and Disney anime style, highly detailed animation, vivid colors, {raw_prompt}"

        print(f"🎬 [{self.name}] جاري طلب المشهد الكرتوني من Replicate...")

        if not self.api_token:
            raise ValueError("مفتاح REPLICATE_API_TOKEN مفقود في GitHub Secrets.")

        try:
            # 1. توليد رابط الفيديو من Replicate
            video_url = replicate.run(
                "minimax/video-01",
                input={
                    "prompt": cartoon_prompt,
                    "prompt_optimizer": True
                }
            )
            print(f"✅ تم استلام رابط الفيديو الأصلي: {video_url}")

            # 2. تنزيل ملف الفيديو والصوت مجاناً
            raw_video_path = "raw_video.mp4"
            audio_path = "temp_voice.mp3"
            
            urllib.request.urlretrieve(str(video_url), raw_video_path)
            speech_text = dialogue_text if dialogue_text else raw_prompt
            asyncio.run(self._generate_speech_audio(speech_text))

            # 3. دمج الصوت مع الفيديو مجاناً باستخدام ffmpeg
            output_final_path = "final_cartoon_video.mp4"
            print(f"🎬 [{self.name}] جاري دمج الصوت والفيديو مجاناً باستخدام ffmpeg...")
            
            cmd = [
                "ffmpeg", "-y",
                "-i", raw_video_path,
                "-i", audio_path,
                "-c:v", "copy",
                "-c:a", "aac",
                "-shortest",
                output_final_path
            ]
            subprocess.run(cmd, check=True)

            print(f"✨ تم إنشاء الفيديو المدمج بنجاح: {output_final_path}")
            return output_final_path

        except Exception as e:
            print(f"❌ حدث خطأ أثناء التوليد أو الدمج: {e}")
            raise e

def generate_cinematic_video(prompt_text: str = "A cheerful cartoon character talking", dialogue_text: str = None):
    agent = VideoAgent()
    return agent.generate_video(prompt_text=prompt_text, dialogue_text=dialogue_text)

if __name__ == "__main__":
    generate_cinematic_video()
