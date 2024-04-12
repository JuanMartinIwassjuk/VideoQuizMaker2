import json
import requests
import audio
import time
import functions_videos
import os
import duracionVideo
from pathlib import Path
import generatorQuiz
from creatomate import Animation, Image, Element, Composition, Source, Video, Audio
from config import NUMBER_OF_QUESTIONS,NUMBER_OF_OPTIONS, LEVEL_OF_DIFFICULTY, TOPIC,BACKGROUND_IMG,AUTORIZACION,TEXTO_PRESENTACION,FONDO_INCIO,BACKGROUND_MUSIC,TEXTO_FINAL,FONDO_VIDEO



#Si se quiere generar automaticamente hay q descomentar esta línea
#data = generatorQuiz.get_openai_response_in_json_format(NUMBER_OF_QUESTIONS,NUMBER_OF_OPTIONS, LEVEL_OF_DIFFICULTY, TOPIC)

data = '{ "questions": [ { "question": "Guess the country:", "options": ["A) Argentina", "B) Brazil", "C) Germany"], "correct_answer": "A) Argentina" }, { "question": "Which country\'s flag is this?:", "options": ["A) Japan", "B) Italy", "C) United States"], "correct_answer": "B) Italy" }, { "question": "Guess the country:", "options": ["A) France", "B) United Kingdom", "C) Canada"], "correct_answer": "C) Canada" }, { "question": "Which country\'s flag is this?", "options": ["A) Russia", "B) China", "C) Australia"], "correct_answer": "A) Russia" }, { "question": "Guess the country:", "options": ["A) India", "B) Mexico", "C) Spain"], "correct_answer": "B) Mexico" }, { "question": "Which country\'s flag is this?", "options": ["A) South Korea", "B) Egypt", "C) South Africa"], "correct_answer": "C) South Africa" }, { "question": "Guess the country:", "options": ["A) Sweden", "B) Switzerland", "C) Norway"], "correct_answer": "A) Sweden" }, { "question": "Which country\'s flag is this?", "options": ["A) Greece", "B) Turkey", "C) Portugal"], "correct_answer": "B) Turkey" } ] }'

background_list_dict = json.loads(BACKGROUND_IMG)


quiz_data_dict=json.loads(data)


audioDrive=[]
audioDriveRtaCorrecta=[]
opcionesCorrectas=[]
    
ruta_audios = Path.cwd() / 'audio'
#if ((generatorQuiz.verificar_archivo_vacio()==False) & (generatorQuiz.es_la_misma_que_anterior(NUMBER_OF_QUESTIONS,NUMBER_OF_OPTIONS, LEVEL_OF_DIFFICULTY, TOPIC)==False)): # Si hay algo y no es la misma q la anterior
#audio.eliminar_archivos_en_ruta(ruta_audios)

text_start_anim = Animation(
    time="start s",
    duration="1.5 s",
    easing="quadratic-out",
    type="text-slide",
    scope="split-clip",
    split="line",
    distance="100%",
    direction="right",
    background_effect="disabled"
)

text_end_anim = Animation(
    time="end",
    duration="1 s",
    easing="quadratic-out",
    type="text-slide",
    direction="left",
    split="line",
    scope="element",
    distance="200%",
    reversed=True
)

comp_start_anim = Animation(
    time="start",
    duration="1 s",
    transition=True,
    type="wipe",
    fade=False,
    x_anchor="0%",
    end_angle="270°",
    start_angle="270°"
)



transition_audio_drive='https://drive.google.com/file/d/138aPIx4loqSwwgsJl0uMeDodoh0978eJ/view?usp=sharing'

countdown_audio_drive='https://drive.google.com/file/d/14VWoFOFrfkBViPbyXM6aJBECn-95qZ3w/view?usp=sharing'

ruta_audio_correcta_drive='https://drive.google.com/file/d/1dZQS5rdjIBmy59rlY34gJFBP7L8gG_4c/view?usp=sharing'

audio_optionDrive='https://drive.google.com/file/d/1IWwxXh3EO7DmKhD-65DX9wZ6tX49biQh/view?usp=sharing'

audio_final_speech_drive='https://drive.google.com/file/d/1JcxYhgcgipCRbHezSUKhi8QBXLgJdonA/view?usp=sharing'

countdown_effect_audio_drive='https://drive.google.com/file/d/1iW1u8i69hC6nkN1T0eVcJnlt_OTCJH0y/view?usp=sharing'

countdown_audio = Path.cwd() / 'audiosEstaticos' / 'countdown.mp3'

transition_audio = Path.cwd() / 'audiosEstaticos' / 'transition.mp3'

ruta_audio_correcta = Path.cwd() / 'audiosEstaticos' / 'correct.mp3'

ruta_speech_final = Path.cwd() / 'audiosEstaticos' /'final_speech.mp3'


#duracion_video,duraciones_preguntas,duracion_presentacion,duracion_parte_final=duracionVideo.get_duraciones(quiz_data_dict,opcionesCorrectas)
#source = Source('mp4', 1080, 1920, duracion_video)
#background_music = Audio("Music", 18, "0 s", None, True, str(BACKGROUND_MUSIC), "6%", "1 s") # Si se quiere poner una fondo En el video
#source.elements.append(background_music)
#video = Video(source)
#animation = Animation(easing='linear', type='scale', scope='element', start_scale='120%', fade=False)

if len(list(ruta_audios.glob("*"))) == 0: # cuando no haya nada
    audio.download_questions_audios_local(quiz_data_dict["questions"])

audio.cargarOpcionesCorrectas(quiz_data_dict["questions"],opcionesCorrectas)

'''
while True:  #Espera a que se suban todos los archivos de forma local
    if len(list(ruta_audios.glob("*"))) >= NUMBER_OF_QUESTIONS:
        break
    time.sleep(1)
'''
estado=True

for index_pregunta, question in enumerate(quiz_data_dict["questions"]):#Esto sube los audios desde local a drive
    if(estado):
        estado=False
        #urlDrive = audio.upload_file_to_google_drive(os.getcwd()+'/audio'+'/'+str(index_pregunta)+'.mp3', '/audio'+'/'+str(index_pregunta)+'.mp3')
        audioDrive.append('https://drive.google.com/file/d/1YUoJ0MSr212pjON5utc65UJmGXeXH2FM/view?usp=sharing')
    else :
        estado=True
        audioDrive.append('https://drive.google.com/file/d/1pQQ9I-nBpUO2ZqdPdgBh6yM54fa-SoN2/view?usp=sharing')

    urlDriveCorrecta = audio.upload_file_to_google_drive(os.getcwd()+'/audio'+'/'+str(index_pregunta)+"-correct"+'.mp3', '/audio'+'/'+str(index_pregunta)+'.mp3')
    audioDriveRtaCorrecta.append(urlDriveCorrecta)
urlDrive = audio.upload_file_to_google_drive(os.getcwd()+'/audio'+'/'+str(NUMBER_OF_QUESTIONS)+'.mp3', '/audio'+'/'+str(NUMBER_OF_QUESTIONS)+'.mp3')#es el texto inicial
audioDrive.append(urlDrive)


'''
while True:  #Espera a que se suban todos los archivos al Drive
    if audio.obtener_cantidad_archivos_en_carpeta(urlDrive) >= NUMBER_OF_QUESTIONS:
        time.sleep(10)
        break
    time.sleep(1)    
'''

duracion_video,duraciones_preguntas,duracion_presentacion,duracion_parte_final=duracionVideo.get_duraciones(quiz_data_dict,opcionesCorrectas)
#Presentacion

source = Source('mp4', 1080, 1920, duracion_video)


#background_music = Audio("Music", 18, "0 s", None, True, str(BACKGROUND_MUSIC), "6%", "1 s")
#source.elements.append(background_music)
video = Video(source)

animation = Animation(easing='linear', type='scale', scope='element', start_scale='120%', fade=False)

composition = Composition("fondovideo", 1,audio.restar_tiempos(duracion_video,duracion_parte_final))
background_video = Image(type="video", source=str(FONDO_VIDEO), track=1, time=0, duration=audio.tiempo_a_float(duracion_video), clip=True,volume="0%",animations=[])
background_video.animations.append(animation)
composition.elements.append(background_video)
logo = Image("https://drive.google.com/file/d/1BlmrY0pIuzFBqlRdblIyeyAAV8WQ8cNE/view?usp=drive_link", track=50,duration=duracion_video,clip=False,animations=[],border_radius="50 vmin",x="85%" ,y="11.80%", width="12%", height="6%", time="0 s")
composition.elements.append(logo)

source.elements.append(composition)

composition1 = Composition("Presentation", 2,duracion_presentacion)
elemento1 = Element("text", track=41, text='It is not easy', fill_color="#ffffff", x="50%", y="25%", font_size="25vmin", width=800,font_weight=600, height=400, x_alignment="0%", y_alignment="0%", letter_spacing="50%", font_family="Rubik")
elemento1.animations.append(text_start_anim)
elemento1.animations.append(text_end_anim)
elemento2 = Element("text", track=44, text='to get a 10/10', fill_color="#ffffff", x="50%", y="45%", font_size="25vmin", width=800,font_weight=600, height=400, x_alignment="0%", y_alignment="0%", letter_spacing="50%", font_family="Rubik")
elemento2.animations.append(text_start_anim)
elemento2.animations.append(text_end_anim)
elemento3 = Element("text", track=45, text='Let\'s get started!!', fill_color="#ffffff", x="50%", y="65%", font_size="25vmin", width=800,font_weight=600, height=400, x_alignment="0%", y_alignment="0%", letter_spacing="50%", font_family="Rubik")
elemento3.animations.append(text_start_anim)
elemento3.animations.append(text_end_anim)
elemento1.stroke_color = "#000000"
elemento2.stroke_color = "#000000"
elemento3.stroke_color = "#000000"
composition1.elements.append(elemento1)
composition1.elements.append(elemento2)
composition1.elements.append(elemento3)
inicial_text_to_speech = Audio("Audio" + str(NUMBER_OF_QUESTIONS), 3, "0 s", audio.obtener_duracion_mp3_en_segundos(os.path.abspath(os.path.join(os.getcwd(), 'audio', str(NUMBER_OF_QUESTIONS)+".mp3"))), True, audioDrive[NUMBER_OF_QUESTIONS], "100%", "0 s")
composition1.elements.append(inicial_text_to_speech)
background_video = Image(type="video", source=str(FONDO_INCIO), track=1, time=0, duration=audio.tiempo_a_float(duracion_presentacion), clip=True,volume="0%")#animations=[]{ "duration": 1, "easing": "cubic-in-out", "transition": True, "type": "slide", "fade": False, "direction": "180°" }
background_video.animations.append(animation)
composition1.elements.append(background_video)
source.elements.append(composition1)

nof = 0
#Generacion de las preguntas
for index_pregunta, question in enumerate(quiz_data_dict["questions"]):
    #count_questions = Element("text", track=234, text=str(nof)+'/'+str(NUMBER_OF_QUESTIONS), x="85%", y="95%", z_index=1, time="0 s", duration=duraciones_preguntas[index_pregunta], fill_color="#ffffff", font_size="8 vmin", font_weight="450",stroke_color="#000000",x_alignment="50%",y_alignment="0")
    #composition.elements.append(count_questions)
    nof=nof+1
    duracion_pregunta="0 s"
    composition = Composition("Question" + str(index_pregunta), 2, duraciones_preguntas[index_pregunta])
    first_track=10
    background_color= [ {"time": "0 s", "value": "rgba(0, 0, 0, 0.5)"}, {"time": audio.restar_tiempos(duraciones_preguntas[index_pregunta],"1 s"),"value": "rgba(0, 0, 0, 0.5)"} ]
    question_text = Element("text", track=3, text=question["question"], y="21.80%", fill_color="#ffffff", background_color="rgba(0, 0, 0, 0.5)",font_size="15 vmin",x_alignment="50%",y_alignment="5%",width="90.48%", height="10.12%",font_family="Rubik", font_weight="400", font_size_maximum="100 vmin",stroke_width="1.5 vmin",letter_spacing="0%")
    question_text.animations.append(text_start_anim)
    question_text.animations.append(text_end_anim)
    question_text.stroke_color = "#000000"
    question_text.background_color = background_color    
    composition.elements.append(question_text)

    duracion_audio_pregunta = audio.obtener_duracion_mp3_en_segundos(os.path.abspath(os.path.join(os.getcwd(), 'audio', f"{index_pregunta}.mp3")))
    ruta_audio_correcto_pregunta = os.path.abspath(os.path.join(os.getcwd(), 'audio', f"{index_pregunta}-correct.mp3"))
    duracion_audio_correcto_pregunta =audio.obtener_duracion_mp3_en_segundos(ruta_audio_correcto_pregunta)

    duracion_pregunta=audio.sumar_tiempos(duracion_audio_pregunta,duracion_pregunta)
    
    question_to_speech = Audio("Audio" + str(index_pregunta), first_track, "0 s", duracion_audio_pregunta, True, audioDrive[index_pregunta], "100%", "0 s")
    composition.elements.append(question_to_speech)

    #background_video = Image(type="video", source=background_list_dict[index_pregunta], track=1, time=0, duration=audio.tiempo_a_float(duraciones_preguntas[index_pregunta]), clip=True)
    #background_video.animations.append(animation)

    #composition.elements.append(background_video)
    #logo = Image("https://drive.google.com/file/d/1BlmrY0pIuzFBqlRdblIyeyAAV8WQ8cNE/view?usp=drive_link", track=50,duration=duracion_video,clip=False,animations=[],border_radius="50 vmin",x="85%" ,y="11.80%", width="12%", height="6%", time="0 s")

    question_img = Image(type="image", source=background_list_dict[index_pregunta], track=index_pregunta+757, time=0, duration=((audio.tiempo_a_float(duraciones_preguntas[index_pregunta]))-1),clip=False,animations=[],border_radius="5 vmin",x="50%" ,y="40%", width="70%", height="20%")
    composition.elements.append(question_img)


    counter = Image("https://i.pinimg.com/originals/3d/c3/87/3dc387151b115cf7ae0cf344b8e40eff.gif", track=46,time=duracion_audio_pregunta,duration="5 s",clip=False,type="video",animations=[], y="7%", width="18%", height="10%",border_radius="50 vmin")
    composition.elements.append(counter)

    second_track=first_track+10
    countdown = Audio("countdown", second_track, duracion_audio_pregunta, "5 s", True, countdown_audio_drive, "5%", "0 s")
    composition.elements.append(countdown)
    third_track=second_track+10
    tiempo_audio_correct= audio.sumar_tiempos(duracion_audio_pregunta,"5.1 s")#donde empieza a sonar audio correcto

    duracion_pregunta=audio.sumar_tiempos("5.1 s",duracion_pregunta)

    tiempo_max_timer=duracion_pregunta

    duracion_audio_correcto=audio.obtener_duracion_mp3_en_segundos(ruta_audio_correcta)

    correct = Audio("correct", third_track, tiempo_audio_correct, duracion_audio_correcto, True, ruta_audio_correcta_drive, "30%", "0 s")

    tiempo_max_sonido_correcto=audio.sumar_tiempos(tiempo_audio_correct,duracion_audio_correcto)

    duracion_pregunta=audio.sumar_tiempos(duracion_audio_correcto,duracion_pregunta)

    composition.elements.append(countdown)
    composition.elements.append(correct)

    
    duracion_char_audio=audio.obtener_duracion_mp3_en_segundos(audio.pathOptionAudio(opcionesCorrectas[index_pregunta]))
    char_option_audio_to_speech = Audio("Audio" +str(index_pregunta)+"-charcorrect", 395,tiempo_audio_correct, duracion_char_audio, True, audio.obtenerRutaDriveCharOption(opcionesCorrectas[index_pregunta]), "100%", "0 s")
    composition.elements.append(char_option_audio_to_speech) #Audio que dice el char de la opcion



    tiempo_max=audio.sumar_tiempos(tiempo_audio_correct,duracion_char_audio)
    content_option_correct_to_speech = Audio("Audio" + str(index_pregunta)+"-correct", 401,audio.sumar_tiempos(tiempo_max,"0.5 s"), audio.obtener_duracion_mp3_en_segundos(os.getcwd()+'/audio'+'/'+str(index_pregunta)+"-correct"+'.mp3'), True, audioDriveRtaCorrecta[index_pregunta], "100%", "0 s")
    composition.elements.append(content_option_correct_to_speech) #Audio que menciona el contenido de la respuesta correcta



    if(index_pregunta<NUMBER_OF_QUESTIONS-1):
        duracion_transicion="1 s"
        ta = Audio("transition", 87, audio.sumar_tiempos(tiempo_max_sonido_correcto,"1.2 s"),duracion_transicion, True, transition_audio_drive, "30%", "0 s")

        duracion_pregunta=audio.sumar_tiempos("1.2 s",duracion_pregunta)#la espera del sonido de transicion


        duracion_pregunta=audio.sumar_tiempos(duracion_transicion,duracion_pregunta)#duracion sonido de transicion

        composition.elements.append(ta)

    #if index_pregunta > 0:
    #    composition.animations.append(comp_start_anim) 
    stroke_color = [ {"time": "0 s", "value": "#000000"}, {"time": tiempo_max_timer, "value": "#000000"}, {"time": duraciones_preguntas[index_pregunta], "value": "#00ff00"} ]
    #background_color= [ {"time": "0 s", "value": "rgba(0, 255, 0, 0)"}, {"time": tiempo_max_timer, "value": "rgba(0, 255, 0, 0)"}, {"time": audio.restar_tiempos(duraciones_preguntas[index_pregunta],"0.5 s"), "value": "#00ff00"} ]
    animationCorrecta = Animation(easing='linear', type='wiggle', scope='element', start_scale='120%', fade=False,time=tiempo_max_timer,duration=duracion_audio_correcto)
    for index_opcion, option in enumerate(question["options"]):
        position_y = 60 + (10 * index_opcion)
        option_text = Element("text", track=index_opcion + 4, text=option, y=str(position_y) + "%", fill_color="#ffffff",x_alignment="0%",y_alignment="5%",x="55%",width="70.48%", height="6.12%",font_family="Rubik", font_weight="400", font_size_maximum="100 vmin",stroke_width="1.5 vmin",letter_spacing="0%")
        option_text.animations.append(text_start_anim)
        option_text.animations.append(text_end_anim)

        if index_opcion == functions_videos.encontrar_indice(quiz_data_dict["questions"][index_pregunta]["options"],quiz_data_dict["questions"][index_pregunta]["correct_answer"]):
            option_text.stroke_color = stroke_color
            #option_text.background_color = background_color
            option_text.animations.append(animationCorrecta)
        else:
            option_text.stroke_color = "#000000"
        
        composition.elements.append(option_text)

    j=0
    for i in range(5):
        inicio_tiempo=time=audio.sumar_tiempos(duracion_audio_pregunta,(str(j)+' s'))
        countdown_text_number = Element("text", track=12, text=str(5 - i), x="49.5%", y="10%", z_index=1, time=inicio_tiempo, duration="1 s", fill_color="#ffffff", font_size="12 vmin", font_weight="400",stroke_color="#000000",x_alignment="50%",y_alignment="5%")
        countdown_effect_audio = Audio("countdown_effect", 894, inicio_tiempo, "1 s", True, countdown_effect_audio_drive, "30%", "0 s")
        j=j+1
        composition.elements.append(countdown_text_number)
        composition.elements.append(countdown_effect_audio)

    source.elements.append(composition)


#Final

composition = Composition("Final",1,duracion_parte_final)
final_text = Element("text", track=889, text=str(TEXTO_FINAL), y="50%", fill_color="#ffffff", background_color="rgba(0, 0, 0, 0.5)",x_alignment="0%",y_alignment="0%")
#final_text = Element("text", track=889, text=str(TEXTO_FINAL), fill_color="#ffffff",x="50%",y="25%",font_size="10 vmin",width=750,height=10,x_alignment="0%",y_alignment="0%")
final_text.animations.append(text_start_anim)
final_text.animations.append(text_end_anim)
final_text.stroke_color = "#000000"
composition.elements.append(final_text)
final_text_to_speech = Audio("Audio" + str(NUMBER_OF_QUESTIONS+1), 334, "0 s", audio.obtener_duracion_mp3_en_segundos(ruta_speech_final), True, audio_final_speech_drive, "100%", "0 s")
composition.elements.append(final_text_to_speech)
animation = Animation(easing='linear', type='scale', scope='element', start_scale='120%', fade=False)
background_video = Image(type="video", source=str(FONDO_INCIO), track=888, time=0, duration=audio.tiempo_a_float(duracion_parte_final), clip=True,volume="0%")
background_video.animations.append(animation)
composition.elements.append(background_video)
source.elements.append(composition)


output = json.loads(video.toJSON())
response = requests.post(
 'https://api.creatomate.com/v1/renders',
 headers={
  'Authorization': 'Bearer '+str(AUTORIZACION),
  'Content-Type': 'application/json',
 },
 json=output
)

if response.status_code >= 200 & response.status_code<300:  # Código 200 indica éxito
    print("La solicitud a createToMate fue exitosa con el codido: ",response.status_code)
else:
    print("La solicitud falló con el código de estado:", response.status_code)
    print("Mensaje de error:", response.text)  # Imprimir el mensaje de error si hay uno

