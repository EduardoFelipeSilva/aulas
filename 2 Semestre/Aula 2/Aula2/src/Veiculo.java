// nome classe UpperCase
public class Veiculo {

        // nome variavel camelCase

        public String modeloCarro, cor;
        public int placa;
        private String marcaCarro;

        public void cadastrar(){
            validarPlaca();
            System.out.println("A cor é: "+cor);
            System.out.println("O modelo do carro é: "+modeloCarro);
        }

        public void atualizar(){

        }

        public String consultar(){
            return "Teste";
        }

        private void validarPlaca(){

        }

    
}
