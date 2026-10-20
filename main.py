from agents.director import DirectorAgent
from agents.visual_prompter import VisualPrompterAgent
from agents.video_agent import VideoAgent

def run_pipeline():
    print("=== تشغيل نظام الوكلاء السينمائي المستقل (كامل) ===")
    
    user_idea = "مدينة مستقبلية تحت الماء في عام 2099"
    print(f"\n[النظام]: تم استلام الفكرة السينمائية: '{user_idea}'\n")
    
    # 1. تهيئة الوكلاء الثلاثة
    director = DirectorAgent("مخرج السينما الآلي")
    prompter = VisualPrompterAgent("مهندس البصريات")
    video_producer = VideoAgent("منتج الفيديو السينمائي")
    
    # 2. توليد السيناريو والأوامر البصرية
    scenes = director.generate_script(user_idea)
    visual_prompts = prompter.build_prompts(scenes)
    
    # 3. خط إنتاج الفيديو والتخزين
    generated_files = []
    for item in visual_prompts:
        video_file = video_producer.generate_video(
            visual_prompt=item['generated_prompt'],
            scene_id=item['scene_id']
        )
        generated_files.append(video_file)
        
    print("\n========================================")
    print("===  النتائج النهائية لنظام الوكلاء  ===")
    print("========================================")
    print(f"[النظام]: تم إنتاج كافة المشاهد السينمائية بنجاح!")
    for file in generated_files:
        print(f" - ملف الفيديو المولد: {file}")
    print("========================================")

if __name__ == "__main__":
    run_pipeline()
