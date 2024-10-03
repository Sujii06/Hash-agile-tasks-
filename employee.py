import pandas as pd
class EmployeeCollection:
    def __init__(self):
        self.collections = {}

    def createCollection(self, collection_name):

        if collection_name not in self.collections:
            self.collections[collection_name] = pd.DataFrame()
            print(f"Collection '{collection_name}' created.")
        else:
            print(f"Collection '{collection_name}' already exists.")

    def indexData(self, collection_name):

        if collection_name in self.collections:
            try:
                df = pd.read_csv('employee data.csv', encoding='ISO-8859-1')  # Specify encoding

                self.collections[collection_name] = df
                print(f"Data indexed in collection '{collection_name}'.")
            except Exception as e:
                print(f"An error occurred while indexing data: {e}")
        else:
            print(f"Collection '{collection_name}' does not exist.")

    def searchByColumn(self, collection_name, column_name, column_value):

        if collection_name in self.collections:

            column_name = column_name.strip()
            try:
                result = self.collections[collection_name][
                    self.collections[collection_name][column_name] == column_value]
                print(f"Search results for {column_name} = '{column_value}' in '{collection_name}':")
                print(result)
                return result
            except KeyError:
                print(f"Column '{column_name}' not found in collection '{collection_name}'.")
            except Exception as e:
                print(f"An error occurred during the search: {e}")
        else:
            print(f"Collection '{collection_name}' does not exist.")

    def getEmpCount(self, p_collection_name):

        if p_collection_name in self.collections:
            collection = self.collections[p_collection_name]
            print(f"Collection '{p_collection_name}' contains {len(collection)} employee's.")
            return len(collection)
        else:
            print(f"Collection '{p_collection_name}' does not exist.")

    def delEmpById(self, collection_name, employee_id):

        if collection_name in self.collections:
            try:

                self.collections[collection_name].columns = self.collections[collection_name].columns.str.strip()
                self.collections[collection_name] = self.collections[collection_name][
                    self.collections[collection_name]['Employee ID'] != employee_id]
                print(f"Employee with ID '{employee_id}' deleted from collection '{collection_name}'.")
            except KeyError:
                print(f"'Employee ID' column not found in collection '{collection_name}'.")
            except Exception as e:
                print(f"An error occurred while deleting employee: {e}")
        else:
            print(f"Collection '{collection_name}' does not exist.")

    def getDepFacet(self, collection_name):

        if collection_name in self.collections:
            try:
                dep_counts = self.collections[collection_name]['Department'].value_counts()
                print(f"Department facet counts for '{collection_name}':")
                print(dep_counts)
                return dep_counts
            except KeyError:
                print(f"Column 'Department' not found in collection '{collection_name}'.")
            except Exception as e:
                print(f"An error occurred while getting department facet: {e}")
        else:
            print(f"Collection '{collection_name}' does not exist.")


if __name__ == "__main__":
    emp_collection = EmployeeCollection()

    v_nameCollection = 'Hash_Suji'
    v_phoneCollection = 'Hash_0477'

    emp_collection.createCollection(v_nameCollection)
    emp_collection.createCollection(v_phoneCollection)

    emp_collection.indexData(v_nameCollection)
    emp_collection.indexData(v_phoneCollection)

    emp_collection.getEmpCount(v_nameCollection)

    emp_collection.delEmpById(v_nameCollection, 'E02003')  # Example employee ID
    emp_collection.getEmpCount(v_nameCollection)
    emp_collection.searchByColumn(v_nameCollection, 'Department', 'IT')
    emp_collection.searchByColumn(v_nameCollection, 'Gender', 'Male')
    emp_collection.searchByColumn(v_phoneCollection, 'Department', 'IT')
    emp_collection.getDepFacet(v_nameCollection)
    emp_collection.getDepFacet(v_phoneCollection)
