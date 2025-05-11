# generate_audio_manifest.py
import os, json

audio_dir = 'audio'
manifest = {}

# Loop over each subfolder in audio/
for folder in sorted(os.listdir(audio_dir)):
    folder_path = os.path.join(audio_dir, folder)
    if os.path.isdir(folder_path):
        # find all .mp3 files
        files = sorted(f for f in os.listdir(folder_path) if f.lower().endswith('.mp3'))
        manifest[folder] = [f'{audio_dir}/{folder}/{f}' for f in files]

# write out audio/manifest.json
out_path = os.path.join(audio_dir, 'manifest.json')
with open(out_path, 'w') as f:
    json.dump(manifest, f, indent=2)
print(f'✅ Written {out_path} with {len(manifest)} entries.')
