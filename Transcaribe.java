package org.example;

import java.util.*;
import java.util.regex.Pattern;

public class Transcaribe {
    static List<Usuario> usuarios = new ArrayList<>(Arrays.asList(
            new Usuario("elias", "123"),
            new Usuario("andres", "321"),
            new Usuario("juan", "000"),
            new Usuario("maria", "111")
    ));
    static Map<String, String> opiniones = new HashMap<>();
    static Map<String, String> recargarTarjeta = new HashMap<>();

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("\n¡Menú de registro!");
            System.out.println("1. Registro");
            System.out.println("2. Iniciar sesión");
            System.out.println("3. Mi opinión");
            System.out.println("4. Salir");

            String choice = scanner.nextLine();

            switch (choice) {
                case "1":
                    registrar(scanner);
                    break;
                case "2":
                    if (iniciarSesion(scanner)) {
                        iniciarRecarga(scanner);
                    }
                    break;
                case "3":
                    darOpinion(scanner);
                    break;
                case "4":
                    System.out.println("Cerrando el programa... ¡Hasta pronto :)!");
                    return;
                default:
                    System.out.println("Opción no válida. Por favor, ingrese una opción correcta.");
                    break;
            }
        }
    }

    public static boolean iniciarSesion(Scanner scanner) {
        int intentos = 0;
        int maxIntentos = 5;

        while (intentos < maxIntentos) {
            System.out.print("Ingrese su nombre de usuario: ");
            String username = scanner.nextLine();

            if (!validarLetras(username)) {
                System.out.println("El nombre de usuario solo puede contener letras.");
                continue;
            }

            System.out.print("Ingrese su contraseña: ");
            String password = scanner.nextLine();

            if (login(username, password)) {
                System.out.println("Inicio de sesión exitoso.");
                System.out.println("¡Bienvenido al portal de compra digital de Transcaribe!");
                return true;
            } else {
                intentos++;
                System.out.println("Nombre de usuario o contraseña incorrectos. Intente nuevamente.");
                System.out.println("Intentos restantes: " + (maxIntentos - intentos));
            }
        }

        if (intentos == maxIntentos) {
            System.out.println("Número máximo de intentos alcanzado. Cerrando el programa.");
        }

        return false;
    }

    public static boolean login(String username, String password) {
        return usuarios.stream()
                .anyMatch(u -> u.getNombre().equals(username) && u.getContraseña().equals(password));
    }

    public static boolean validarLetras(String texto) {
        return Pattern.matches("^[a-zA-Z]+$", texto);
    }

    public static boolean validarNumeros(String texto) {
        return Pattern.matches("^[0-9]+$", texto);
    }

    public static boolean validarCorreo(String correo) {
        return Pattern.matches("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$", correo);
    }

    public static boolean validarMetodoPago(String metodoPago) {
        List<String> metodosValidos = Arrays.asList("nequi", "daviplata", "tarjeta de debito", "pse");
        return metodosValidos.contains(metodoPago.toLowerCase());
    }

    public static void ingresarDatosPago(String metodoPago, Scanner scanner) {
        System.out.println("Ingresando datos para el método de pago: " + metodoPago);

        if (metodoPago.equalsIgnoreCase("nequi") || metodoPago.equalsIgnoreCase("daviplata")) {
            while (true) {
                System.out.print("Ingrese su número de cuenta: ");
                String numeroCuenta = scanner.nextLine();
                if (!validarNumeros(numeroCuenta)) {
                    System.out.println("El número de cuenta solo puede contener números.");
                } else {
                    break;
                }
            }
            System.out.print("Ingrese su contraseña: ");
            scanner.nextLine(); // leer contraseña
            System.out.println("Datos ingresados correctamente.");
        } else if (metodoPago.equalsIgnoreCase("tarjeta de debito")) {
            while (true) {
                System.out.print("Ingrese el número de su tarjeta de débito: ");
                String numeroTarjeta = scanner.nextLine();
                if (!validarNumeros(numeroTarjeta)) {
                    System.out.println("El número de tarjeta solo puede contener números.");
                } else {
                    break;
                }
            }
            System.out.print("Ingrese su contraseña: ");
            scanner.nextLine(); // leer contraseña
            System.out.print("Ingrese su clave dinámica: ");
            scanner.nextLine(); // leer clave dinámica
            System.out.println("Datos ingresados correctamente.");
        } else if (metodoPago.equalsIgnoreCase("pse")) {
            System.out.print("Ingrese su usuario PSE: ");
            scanner.nextLine(); // leer usuario PSE
            System.out.print("Ingrese su contraseña: ");
            scanner.nextLine(); // leer contraseña
            System.out.println("Datos ingresados correctamente.");
        }
    }

    public static void iniciarRecarga(Scanner scanner) {
        while (true) {
            System.out.println("\nMenú de Recarga");
            System.out.println("1. Realizar Recarga");
            System.out.println("2. Registro de Recargas");
            System.out.println("3. Borrar Registro de Recarga");
            System.out.println("4. Cerrar sesión");

            String opcion = scanner.nextLine();

            switch (opcion) {
                case "1":
                    String numeroTarjeta;
                    while (true) {
                        System.out.print("Ingrese el Número de tarjeta de la Recarga: ");
                        numeroTarjeta = scanner.nextLine();
                        if (!validarNumeros(numeroTarjeta)) {
                            System.out.println("El número de tarjeta solo puede contener números.");
                        } else {
                            break;
                        }
                    }

                    System.out.print("Ingrese el monto: $");
                    String monto = scanner.nextLine();
                    if (!validarNumeros(monto)) {
                        System.out.println("El monto solo puede contener números.");
                    } else {
                        System.out.print("Ingrese el método de pago (nequi, daviplata, tarjeta de debito, pse): ");
                        String metodoPago = scanner.nextLine();
                        if (validarMetodoPago(metodoPago)) {
                            ingresarDatosPago(metodoPago, scanner);
                            recargarTarjeta.put(numeroTarjeta, monto);  // Ahora el número de tarjeta es la clave
                            System.out.println("Tarjeta recargada con éxito.");
                        } else {
                            System.out.println("Método de pago no válido.");
                        }
                    }
                    break;
                case "2":
                    mostrarRecargas();
                    break;
                case "3":
                    System.out.print("Ingrese el Número de tarjeta de la Recarga a eliminar: ");
                    String numeroTarjetaEliminar = scanner.nextLine();
                    eliminarRecarga(numeroTarjetaEliminar);
                    break;
                case "4":
                    System.out.println("Sesión cerrada con éxito.");
                    return;
                default:
                    System.out.println("Opción no válida. Por favor, seleccione una opción válida.");
                    break;
            }
        }
    }

    public static void mostrarRecargas() {
        if (!recargarTarjeta.isEmpty()) {
            System.out.println("Lista de Recargas:");
            recargarTarjeta.forEach((tarjeta, monto) -> System.out.println("Número de tarjeta: " + tarjeta + ", Monto: $" + monto));
        } else {
            System.out.println("El registro de recarga está vacío.");
        }
    }

    public static void eliminarRecarga(String numeroTarjeta) {
        if (recargarTarjeta.containsKey(numeroTarjeta)) {
            recargarTarjeta.remove(numeroTarjeta);
            System.out.println("Recarga de la tarjeta " + numeroTarjeta + " eliminada con éxito.");
        } else {
            System.out.println("La recarga de la tarjeta " + numeroTarjeta + " no se encuentra.");
        }
    }


    public static void registrar(Scanner scanner) {
        System.out.println("¡Bienvenido al registro de usuario!");

        String nombre, apellidos, correo, contraseña, confirmarContraseña;
        int edad;

        while (true) {
            System.out.print("Ingresa tu nombre: ");
            nombre = scanner.nextLine();
            if (!validarLetras(nombre)) {
                System.out.println("El nombre solo puede contener letras.");
                continue;
            }

            System.out.print("Ingresa tu apellido: ");
            apellidos = scanner.nextLine();
            if (!validarLetras(apellidos)) {
                System.out.println("El apellido solo puede contener letras.");
                continue;
            }

            System.out.print("Ingresa tu edad: ");
            String edadTexto = scanner.nextLine();
            if (!validarNumeros(edadTexto)) {
                System.out.println("La edad solo puede contener números.");
                continue;
            }

            edad = Integer.parseInt(edadTexto);
            if (edad < 15 || edad > 100) {
                System.out.println("Solo se permiten usuarios de 15 a 100 años.");
                continue;
            }

            while (true) {
                System.out.print("Ingresa tu correo electrónico: ");
                correo = scanner.nextLine();
                if (validarCorreo(correo)) {
                    break;
                } else {
                    System.out.println("El correo electrónico ingresado no es válido. Intente nuevamente.");
                }
            }

            while (true) {
                System.out.print("Ingresa tu contraseña: ");
                contraseña = scanner.nextLine();
                System.out.print("Confirma tu contraseña: ");
                confirmarContraseña = scanner.nextLine();
                if (contraseña.equals(confirmarContraseña)) {
                    break;
                } else {
                    System.out.println("Las contraseñas no coinciden. Intente nuevamente.");
                }
            }

            usuarios.add(new Usuario(nombre.toLowerCase(), contraseña));
            System.out.println("\n¡Gracias por registrarte! Bienvenido :)");
            System.out.println("Nombre: " + nombre);
            System.out.println("Apellido: " + apellidos);
            System.out.println("Edad: " + edad);
            System.out.println("Correo: " + correo);
            break;
        }
    }

    public static void darOpinion(Scanner scanner) {
        System.out.print("Ingrese su nombre de usuario: ");
        String usuario = scanner.nextLine();
        System.out.print("Por favor, escriba su opinión: ");
        String opinion = scanner.nextLine();
        opiniones.put(usuario, opinion);
        System.out.println("¡Gracias por compartir su opinión!");
    }
}

class Usuario {
    private String nombre;
    private String contraseña;

    public Usuario(String nombre, String contraseña) {
        this.nombre = nombre;
        this.contraseña = contraseña;
    }

    public String getNombre() {
        return nombre;
    }

    public String getContraseña() {
        return contraseña;
    }
}
