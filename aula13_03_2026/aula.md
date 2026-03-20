
<h3>Exercício 1: Gerenciamento de Recursos com yield e Teardown</h3>
Contexto

Você está desenvolvendo um sistema que precisa manipular arquivos de log
temporários durante os testes. É fundamental que cada teste tenha seu próprio
arquivo e que, ao final de cada execução, o arquivo seja removido para não poluir o
ambiente.
Tarefa
1. Crie uma fixture chamada log_file que:
• Crie um arquivo chamado test_log.txt no modo de escrita.
• Forneça o objeto do arquivo para o teste usando yield.
• Após o teste, feche o arquivo e o remova do sistema de arquivos (Dica: use
os.remove).
2. Escreva um teste test_escrita_log que utilize essa fixture para escrever a frase
“Teste de log” e verifique se o arquivo não está fechado durante a execução.
Critérios de Avaliação
• Uso correto do yield para separar o Setup do Teardown.
• Garantia de que o recurso foi limpo após o teste.



<h3>Exercício 2: Escopos, autouse e Organização com conftest.py</h3>

Contexto
Em um projeto de grande escala, você tem conexões pesadas com banco de dados que não devem ser reiniciadas a cada teste, mas sim uma vez por sessão. Além disso,você precisa garantir que um “limpador de cache” rode antes de cada função de teste sem precisar chamá-lo manualmente.
Tarefa
1. Estruture um diretório de projeto com a seguinte hierarquia:
projeto/
├── conftest.py
└── test_db.py
2. No conftest.py:
• Crie uma fixture db_connection com scope="session". Ela deve apenas
retornar uma string "Conexão Global Estabelecida".

• Crie uma fixture clean_cache com autouse=True. Ela deve imprimir no
console “Cache limpo antes do teste”.
3. No test_db.py:
• Escreva dois testes simples que verifiquem se a db_connection contém a string
esperada.
• Observe (via pytest -s) se o “Cache limpo” aparece antes de cada teste e se a
conexão é citada.
Critérios de Avaliação
• Implementação correta de escopos para otimização de performance.
• Uso de autouse para tarefas repetitivas e transversais.
• Organização correta de arquivos seguindo o padrão do Pytest.

<h3>Exercício 3: Parametrização Dinâmica de Fixtures</h3>

Contexto
Você precisa validar uma função que processa diferentes tipos de usuários (Admin,
Editor, Visitante). Em vez de criar três testes quase idênticos, você deve usar uma
fixture parametrizada.
Tarefa
1. Crie uma fixture chamada user_data que utilize o parâmetro params para
alternar entre três dicionários:
• {"role": "admin", "access": True}
• {"role": "editor", "access": True}
• {"role": "guest", "access": False}
2. Dentro da fixture, use request.param para acessar os dados.
3. Escreva um teste test_access_control que receba essa fixture e verifique:
• Se o usuário for “guest”, o access deve ser False.
• Caso contrário, deve ser True.
Critérios de Avaliação
• Uso correto do parâmetro params na definição da fixture.
• Acesso aos dados via objeto request.
• Redução de redundância de código através da parametrização.

<h3>comandos</h3>

O parâmetro <b>autouse=True</b> permite que a fixture seja aplicada
automaticamente a todos os testes dentro do seu escopo ( scope ),
eliminando a necessidade de injetar seu nome em cada função de teste (ex:
def test_algo(minha_fixture): ).