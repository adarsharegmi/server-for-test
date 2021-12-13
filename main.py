import pyttsx3
import asyncio
import aiofiles

async def read_text(female=0, store=True, audio_name='') -> None:
    '''
        make use of pyttsx3 library for reading the text and read the files.
    '''
    
    engine = pyttsx3.init() # object creation
    voices = engine.getProperty('voices')       #getting details of current voice
    if female:
        engine.setProperty('voice', voices[1].id)
    text= await read_file()
    engine.say(text)

    ' if to be stored'
    if store:
        engine.save_to_file(text, 'test.mp3') 
        
    engine.runAndWait()
    engine.stop()


async def read_file(file_path='a.txt'):
    '''
        reading the files using the file reader aiofiles for async reading
    '''
    async with aiofiles.open(file_path, mode='r') as f:
        return await f.read()
       
    
if __name__ == '__main__':
    '''
    main method 
    '''
    loop = asyncio.get_event_loop()
    loop.run_until_complete(read_text(female=1, store=True, audio_name='test') )
    loop.close()