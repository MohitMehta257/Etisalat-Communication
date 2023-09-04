import os
import azure.cognitiveservices.speech as speechsdk

speech_config=speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'),region=os.environ.get('SPEECH_REGION'))
audio_config=speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

#speech_config.speech_synthesis_voice_name="en-US-ElizabethNeural"
speech_config.speech_synthesis_language='bn-IN-TanishaaNeural'

speech_synthesizer=speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

print("Enter some text to test")

text=input()

speech_synthesizer_result=speech_synthesizer.speak_text_async(text).get()


if speech_synthesizer_result.reason==speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Speech synthesized for text [{}]".format(text))
elif speech_synthesizer_result.reason==speechsdk.ResultReason.Canceled:
    cancellation_details=speech_synthesizer_result.cancellation_details
    print("Speech synthesis cancelled due to the following reason [{}]".format(cancellation_details.reason))
    if cancellation_details==speechsdk.CancellationReason.Error:
        if cancellation_details.error_details:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")
