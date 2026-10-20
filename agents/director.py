class DirectorAgent:
    def __init__(self, name="Director Alpha"):
        self.name = name

    def generate_script(self, idea_concept):
        """تحويل الفكرة الخام إلى سيناريو سينمائي مقسم لمشاهد"""
        print(f"[{self.name}] جاري تحليل الفكرة وصياغة المشاهد السينمائية...")
        
        scenes = [
            {
                "scene_id": 1,
                "description": f"مشهد افتتاحي درامي يعكس مفهوم: {idea_concept}",
                "lighting": "إضاءة خافتة مع ظلال حادة (Low-key lighting)",
                "camera_angle": "زاوية واسعة وسريعة (Wide Angle Shot)"
            },
            {
                "scene_id": 2,
                "description": f"تركيز عالي وتفاصيل دقيقة تجسد ذروة الأحداث في: {idea_concept}",
                "lighting": "إضاءة سينمائية نحاسية دافئة (Cinematic Warm Gold)",
                "camera_angle": "لقطة قريبة جداً على التفاصيل (Extreme Close-Up)"
            }
        ]
        return scenes
