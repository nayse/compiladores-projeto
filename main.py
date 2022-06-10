from sys import path as sys_path, argv
from utils import Path

main_path = str(Path().script_dir())
sys_path.append(main_path)

from lexicalanalyzer import Lexical


if main_path[len(main_path) - 1] != '/':
  main_path += '/'


def main(file_path=main_path+'teste.pas', output_early=True):
  file = argv[1] if len(argv) > 1 else file_path
  with open(file, 'r') as file:
    tokens = Lexical(file).split()
    print('Análise Léxica bem sucedida. A lista de tokens gerados está disponível no arquivo tokens.log')


    if output_early: generate_output(tokens)

    if not output_early: generate_output(tokens)

  return tokens


def generate_output(tokens):
    print_tokens(tokens)



def print_tokens(tokens):
  with open(main_path + 'tokens.log', 'w') as log:
    for i in tokens:
      log.write("[")
      for c in i:
        log.write(str(c) + ', ')
      log.write("],\n")



if __name__ == '__main__':
  main(output_early=True)
