public class Endereco {
    
    // Estrutura minima de uma classe:
    // Atributos
    // metodos de acesso(Construtor,Getters e Setters)
    // Metodo de validação de entrada de dados


    // Essa classe no mundo a fora é chamada:
    // Classe de dominio, Classe modelo(ou model) ou entidade
    private String logradouro, cidade, bairro, estado, complemento, cep;
    private int numero;
    
    // Tudo em () é considerado um paramentro de entrada de dados
    public Endereco(String logradouro, String cidade, String bairro, String estado,
                    String complemento, String cep, int numero){
                        // Atribuir valores aos atributos mencionados no inicio da classe
                        // this.nome_atributo = paramentro_entrada
                        // this -> mencionar o atributo criado no inicio da classe, pois havera
                        // atributos ou variaveis com nome similares

                        this.logradouro=logradouro;
                        this.cidade=cidade;
                        this.bairro=bairro;
                        this.estado=estado;
                        this.complemento=complemento;
                        this.cep=cep;
                        this.numero=numero;

                    }
        // metodos setters: sao utilizados para atribuir valor a UM atributo
        // Tem o principio de criar ou atualizar um atributo especifico

        public void setLogradouro(String logradouro){
            this.logradouro = logradouro;
        }

        public void setNumero (int numero){
            this.numero = numero;
        }

        // metodos getters: são utilizados para consultar/recureprar o valor de UM atributo

        public String getLogradouro(){
            return this.logradouro;
        }

        public int getNumero(){
            return this.numero;
        }

}
