import os
import platform
import shutil
import datetime
from pathlib import Path

class AssistenteAutomacao:
    """
    Classe principal que gerencia as automações de sistema e documentos.
    """
    def __init__(self):
        self.diretorio_atual = os.getcwd()
        self.pasta_relatorios = os.path.join(self.diretorio_atual, "Relatorios")
        
        # Garante que a pasta de relatórios exista
        if not os.path.exists(self.pasta_relatorios):
            os.makedirs(self.pasta_relatorios)

    def analisar_sistema(self):
        """Coleta informações do sistema operacional e do hardware básico."""
        print("\n🔍 Iniciando Análise do Sistema...")
        
        sistema_info = platform.uname()
        cpu_nucleos = os.cpu_count()
        disco = shutil.disk_usage("/")
        
        # Converte bytes para Gigabytes
        disco_total_gb = disco.total / (1024**3)
        disco_livre_gb = disco.free / (1024**3)

        dados_analise = (
            f"--- ANÁLISE DO SISTEMA ---\n"
            f"Data da Análise: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
            f"Sistema Operacional: {sistema_info.system} {sistema_info.release}\n"
            f"Nome da Máquina: {sistema_info.node}\n"
            f"Processador: {sistema_info.processor}\n"
            f"Núcleos de CPU: {cpu_nucleos}\n"
            f"Armazenamento Total: {disco_total_gb:.2f} GB\n"
            f"Armazenamento Livre: {disco_livre_gb:.2f} GB\n"
            f"--------------------------\n"
        )
        print("Análise concluída com sucesso.")
        return dados_analise

    def criar_relatorio_sistema(self):
        """Gera um arquivo de texto com os dados da análise do sistema."""
        dados = self.analisar_sistema()
        
        # Cria um nome de arquivo único baseado no timestamp
        nome_arquivo = f"relatorio_sistema_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        caminho_completo = os.path.join(self.pasta_relatorios, nome_arquivo)
        
        try:
            with open(caminho_completo, 'w', encoding='utf-8') as arquivo:
                arquivo.write(dados)
            print(f"Documento criado! Relatório salvo em: {caminho_completo}")
        except Exception as e:
            print(f"Erro ao criar o documento: {e}")

    def analisar_documento(self, caminho_arquivo):
        """Analisa um documento de texto (.txt) e extrai estatísticas úteis."""
        if not os.path.exists(caminho_arquivo):
            print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
            return

        print(f"\n🧠 Analisando documento: {caminho_arquivo}...")
        
        try:
            with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
                conteudo = arquivo.read()
                linhas = conteudo.split('\n')
                palavras = conteudo.split()
                
                # Exemplo de análise avançada: buscar palavras-chave de alerta
                palavras_chave = ['erro', 'falha', 'urgente', 'atenção', 'aviso']
                alertas_encontrados = [p for p in palavras if p.lower() in palavras_chave]

            print("\n--- RESULTADO DA ANÁLISE DO DOCUMENTO ---")
            print(f"Total de Linhas: {len(linhas)}")
            print(f"Total de Palavras: {len(palavras)}")
            print(f"Palavras de alerta encontradas: {len(alertas_encontrados)}")
            if alertas_encontrados:
                print(f"⚠️ Alertas detectados: {set(alertas_encontrados)}")
            print("-----------------------------------------")
            
        except Exception as e:
            print(f"Erro ao ler o documento: {e}")

    def executar_menu(self):
        """Menu interativo para o usuário escolher o que fazer."""
        while True:
            print("\n" + "="*40)
            print("PAINEL DE AUTOMAÇÃO AVANÇADA")
            print("="*40)
            print("1 - Fazer análise do sistema na tela")
            print("2 - Criar documento de relatório do sistema")
            print("3 - Analisar um documento de texto")
            print("4 - Sair")
            
            escolha = input("\nEscolha uma opção (1-4): ").strip()
            
            if escolha == '1':
                print(self.analisar_sistema())
            elif escolha == '2':
                self.criar_relatorio_sistema()
            elif escolha == '3':
                arquivo = input("Digite o nome ou caminho do arquivo .txt (ex: meu_texto.txt): ")
                self.analisar_documento(arquivo)
            elif escolha == '4':
                print("Encerrando o sistema. Até logo!")
                break
            else:
                print("Opção inválida. Tente novamente.")

# Bloco de execução principal
if __name__ == "__main__":
    assistente = AssistenteAutomacao()
    assistente.executar_menu()