from agents.director import DirectorAgent
from agents.visual_prompter import VisualPrompterAgent

def run_pipeline():
    print("=== تشغيل نظام الوكلاء السينمائي المستقل ===")
    
    # 1. إدخال الفكرة بشكل مباشر وثابت ليتوافق مع التشغيل السحابي الآلي
    user_idea = "مدينة مستقبلية تحت الماء في عام 2099"
    print(f"\n[النظام]: تم استلام الفكرة بنجاح: '{user_idea}'\n")
    
    # 2. استدعاء الوكلاء
    director = DirectorAgent("مخرج السينما الآلي")
    prompter = VisualPrompterAgent("مهندس البصريات")
    
    # 3. خط الإنتاج (Workflow): المخرج يصنع السيناريو، ثم مهندس البصريات يحوله لأوامر
    scenes = director.generate_script(user_idea)
    visual_prompts = prompter.build_prompts(scenes)
    
    # 4. عرض النتائج النهائية المستخرجة من الوكلاء في السجلات
    print("\n========================================")
    print("===  النتائج النهائية لنظام الوكلاء  ===")
    print("========================================")
    for item in visual_prompts:
        print(f"\n[المشهد رقم {item['scene_id']}]")
        print(f"الأمر البصري الاحترافي: \n{item['generated_prompt']}")
    print("\n========================================")
    print("[النظام]: تمت عملية توليد خط الإنتاج بنجاح تام!")

if __name__ == "__main__":
    run_pipeline()
