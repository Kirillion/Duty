using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace C_SH
{
    static class Program
    {
        /// <summary>
        ///  The main entry point for the application.
        /// </summary>
        /// 

        //Scaffold-DbContext "Host=localhost;Port=5432;Database=usersdb;Username=postgres;Password=password"

        //	 Npgsql.EntityFrameworkCore.PostgreSQL

        [STAThread]
        static void Main()
        {
            Application.SetHighDpiMode(HighDpiMode.SystemAware);
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new Form1());
            
        }
    }
}
/*
  Информационная система – организационно упорядоченная
совокупность документов (массивов документов) и информационных
технологий, в том числе с использованием средств вычислительной
техники и связи, реализующих информационные процессы.
Информационные системы предназначены для хранения, обработки,
поиска, распространения, передачи и предоставления информации.

Архитектура информационной системы – концепция,
определяющая модель, структуру, выполняемые функции и
взаимосвязь компонентов информационной системы.

Интерфейс -> Бизнес логика -> Управление данными
*/

/*
 * Харяга
 * rder Service (Сервис Заказа) создает Order (Заказ) в статусе pending (в ожидании) и публикует событие OrderCreated (ЗаказСоздан)
Customer Service (Сервис Клиента) получает событие и пытается зарезервировать кредит для заказа. После чего публикует одно из двух событий: CreditReserved (КредитЗарезервирован) или CreditLimitExceeded (КредитныйЛимитПревышен)
Order Service (Сервис Заказа) получает событие и изменяет состояние заказа в approved (подтвержден) или cancelled (отменен)
Оркестр
Order Service (Сервис Заказа) создает Order (Заказ) в статусе pending (в ожидании) и создает CreateOrderSaga (СагаСозданияЗаказа)
CreateOrderSaga (СагаСозданияЗаказа) отправляет команду ReserveCredit (ЗарезервироватьКредит) в Customer Service (Сервис Клиента)
Customer Service (Сервис Клиента) пытается зарезервировать кредит для заказа и отправляет назад ответ
CreateOrderSaga (СагаСозданияЗаказа) получает ответ и отправляет ApproveOrder (ПодтвердитьЗаказ) or RejectOrder (ОтменитьЗаказ) команду в Order Service (Сервис Заказа)
Order Service (Сервис Заказа) изменяет состояние заказа в approved (подтвержден) или cancelled (отменен)*/