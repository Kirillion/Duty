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
  �������������� ������� � �������������� �������������
������������ ���������� (�������� ����������) � ��������������
����������, � ��� ����� � �������������� ������� ��������������
������� � �����, ����������� �������������� ��������.
�������������� ������� ������������� ��� ��������, ���������,
������, ���������������, �������� � �������������� ����������.

����������� �������������� ������� � ���������,
������������ ������, ���������, ����������� ������� �
����������� ����������� �������������� �������.

��������� -> ������ ������ -> ���������� �������
*/

/*
 * ������
 * rder Service (������ ������) ������� Order (�����) � ������� pending (� ��������) � ��������� ������� OrderCreated (�����������)
Customer Service (������ �������) �������� ������� � �������� ��������������� ������ ��� ������. ����� ���� ��������� ���� �� ���� �������: CreditReserved (��������������������) ��� CreditLimitExceeded (����������������������)
Order Service (������ ������) �������� ������� � �������� ��������� ������ � approved (�����������) ��� cancelled (�������)
�������
Order Service (������ ������) ������� Order (�����) � ������� pending (� ��������) � ������� CreateOrderSaga (������������������)
CreateOrderSaga (������������������) ���������� ������� ReserveCredit (���������������������) � Customer Service (������ �������)
Customer Service (������ �������) �������� ��������������� ������ ��� ������ � ���������� ����� �����
CreateOrderSaga (������������������) �������� ����� � ���������� ApproveOrder (����������������) or RejectOrder (�������������) ������� � Order Service (������ ������)
Order Service (������ ������) �������� ��������� ������ � approved (�����������) ��� cancelled (�������)*/