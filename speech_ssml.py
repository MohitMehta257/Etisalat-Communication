import os
import azure.cognitiveservices.speech as speechsdk

speech_config=speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'),region=os.environ.get('SPEECH_REGION'))
audio_config=speechsdk.audio.AudioOutputConfig(use_default_speaker=True)


speech_synthesizer=speechsdk.SpeechSynthesizer(speech_config=speech_config,audio_config=audio_config)

ssml_string=open("ssml.xml","r").read()

result=speech_synthesizer.speak_ssml_async(ssml_string).get()

#stream