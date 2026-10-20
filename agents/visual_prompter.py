class VisualPrompterAgent:
    def __init__(self, name="Visual Specialist"):
        self.name = name

    def build_prompts(self, scenes):
        """تحويل المشاهد السينمائية إلى أوامر بصريات عالية الجودة"""
        print(f"[{self.name}] جاري صياغة الأوامر البصرية للمشاهد...")
        prompts = []
        
        for scene in scenes:
            prompt_text = (
                f"Cinematic video frame, {scene['description']}, "
                f"{scene['lighting']}, {scene['camera_angle']}, "
                f"photorealistic, 8k resolution, highly detailed, Unreal Engine 5 render style"
            )
            prompts.append({
                "scene_id": scene["scene_id"],
                "generated_prompt": prompt_text
            })
            
        return prompts
