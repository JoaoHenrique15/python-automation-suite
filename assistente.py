import webbrowser
import datetime
import os
import shutil

# --- FUNÇÕES DE AUTOMAÇÃO ---

def abrir_site():
    print("🌐 Abrindo o navegador...")
    webbrowser.open('https://www.google.com') # Você pode trocar pelo site que quiser

def mostrar_hora():
    agora = datetime.datetime.now()
    print(f"⏰ A data e hora atuais são: {agora.strftime('%d/%m/%Y %H:%M:%S')}")

def organizar_arquivos_simples():
    # Exemplo: Cria uma pasta 'Textos' e move arquivos .txt para lá
    # Aviso: Cuidado ao rodar isso em pastas importantes!
    pasta_atual = os.getcwd()
    pasta_destino = os.path.join(pasta_atual, 'Textos')
    
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)
        
    moveu_algo = False
    for arquivo in os.listdir(pasta_atual):
        if arquivo.endswith('.txt'):
            shutil.move(arquivo, pasta_destino)
            print(f"📄 Arquivo movido: {arquivo}")
            moveu_algo = True
            
    if not moveu_algo:
        print("🤷 Nenhum arquivo .txt encontrado para organizar.")

# --- NÚCLEO DO PROGRAMA ---

def iniciar_assistente():
    print("🤖 Olá! Sou seu assistente de automação em Python.")
    print("Comandos disponíveis: 'site', 'hora', 'organizar', 'sair'")
    print("-" * 40)
    
    while True:
        # Lê o que o usuário digita e converte para minúsculas
        comando = input("\nO que você quer que eu faça? ").lower().strip()
        
        if comando == 'sair':
            print("👋 Encerrando o assistente. Até mais!")
            break
        elif comando == 'site':
            abrir_site()
        elif comando == 'hora':
            mostrar_hora()
        elif comando == 'organizar':
            organizar_arquivos_simples()
        else:
            print("❌ Comando não reconhecido. Tente usar uma das opções disponíveis.")

# Garante que o script só rode se for executado diretamente
if __name__ == "__main__":
    iniciar_assistente()